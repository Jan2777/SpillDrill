import React, { useState, useEffect, useRef, useCallback } from 'react';
import { StyleSheet, View, TouchableOpacity, Text, Animated, Easing, Alert } from 'react-native';
import MapView, { Marker } from 'react-native-maps';
import * as Location from 'expo-location';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { Audio } from 'expo-av';
import Sidebar from './components/Sidebar';
import Settings from './components/Setting'; // Adjust path as needed
import Alerts from './components/Alerts';
import Profile from './components/Profile';
import Report from './components/Report';
import OilSpillPrediction from './components/OilSpill';
import data from './assets/data'; // Ensure this path is correct
import { Ionicons } from '@expo/vector-icons'; // Import icons

const Drawer = createDrawerNavigator();

const HomeScreen = ({ navigation }) => {
  const mapRef = useRef(null);
  const [location, setLocation] = useState({
    latitude: 20,
    longitude: 0,
  });

  const [mapRegion, setMapRegion] = useState({
    latitude: 20,
    longitude: 0,
    latitudeDelta: 0.0922, // More reasonable delta for smoother zoom
    longitudeDelta: 0.0421, // More reasonable delta for smoother zoom
  });

  const [zoomAnimation] = useState(new Animated.Value(1));
  const [previousTimestamp, setPreviousTimestamp] = useState(data.timestamp);
  const [sound, setSound] = useState(null);

  useEffect(() => {
    const initialize = async () => {
      try {
        let { status } = await Location.requestForegroundPermissionsAsync();
        if (status !== 'granted') {
          alert('Permission to access location was denied');
          return;
        }

        let currentLocation = await Location.getCurrentPositionAsync({});
        setLocation({
          latitude: currentLocation.coords.latitude,
          longitude: currentLocation.coords.longitude,
        });

        setMapRegion((prevRegion) => ({
          ...prevRegion,
          latitude: currentLocation.coords.latitude,
          longitude: currentLocation.coords.longitude,
        }));

        const { sound: beepSound } = await Audio.Sound.createAsync(
          require('./assets/beep.mp3') // Ensure this path is correct
        );
        setSound(beepSound);

        checkForDataChanges();
      } catch (error) {
        console.error(error);
      }
    };

    initialize();
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      checkForDataChanges();
    }, 10000); // Check every 10 seconds

    return () => clearInterval(interval);
  }, [previousTimestamp]);

  const checkForDataChanges = useCallback(() => {
    const currentTimestamp = data.timestamp;

    if (currentTimestamp !== previousTimestamp) {
      playSound();
      const newSpill = data.spills[0]; // Assuming the new spill is at index 0; adjust logic as needed
      Alert.alert(
        "Alert",
        `New spill detected at ${newSpill.Location} with coordinates (${newSpill.Latitude}, ${newSpill.Longitude})`,
        [{ text: "OK", onPress: () => zoomToSpill(newSpill) }]
      );
      setPreviousTimestamp(currentTimestamp);
    }
  }, [previousTimestamp]);

  const playSound = async () => {
    if (sound) {
      await sound.playAsync();
    }
  };

  const animateButton = () => {
    Animated.sequence([
      Animated.timing(zoomAnimation, {
        toValue: 1.1,
        duration: 200,
        easing: Easing.ease,
        useNativeDriver: true,
      }),
      Animated.timing(zoomAnimation, {
        toValue: 1,
        duration: 200,
        easing: Easing.ease,
        useNativeDriver: true,
      }),
    ]).start();
  };

  const zoomIn = () => {
    animateButton();
    mapRef.current.animateToRegion({
      ...mapRegion,
      latitudeDelta: mapRegion.latitudeDelta / 1.5,
      longitudeDelta: mapRegion.longitudeDelta / 1.5,
    }, 500);
  };

  const zoomOut = () => {
    animateButton();
    mapRef.current.animateToRegion({
      ...mapRegion,
      latitudeDelta: mapRegion.latitudeDelta * 1.5,
      longitudeDelta: mapRegion.longitudeDelta * 1.5,
    }, 500);
  };

  const zoomToSpill = (spill) => {
    mapRef.current.animateToRegion({
      latitude: spill.Latitude,
      longitude: spill.Longitude,
      latitudeDelta: 0.05,
      longitudeDelta: 0.05,
    }, 500);
  };

  return (
    <View style={styles.container}>
      <MapView
        ref={mapRef}
        style={styles.map}
        region={mapRegion}
        onRegionChangeComplete={(region) => setMapRegion(region)}
        showsUserLocation
        loadingEnabled
        showsCompass
        zoomControlEnabled={false}
        moveOnMarkerPress={false}
      >
        {data.spills ? data.spills.map((spill, index) => (
          <Marker
            key={index}
            coordinate={{
              latitude: spill.Latitude,
              longitude: spill.Longitude,
            }}
            title={spill.Location}
            description={spill.Type}
          />
        )) : null}
        <Marker
          coordinate={location}
          title="My Location"
          pinColor="blue"
        />
      </MapView>

      <View style={styles.buttonContainer}>
        <Animated.View style={{ transform: [{ scale: zoomAnimation }] }}>
          <TouchableOpacity style={styles.zoomButton} onPress={zoomIn}>
            <Text style={styles.zoomButtonText}>Zoom In</Text>
          </TouchableOpacity>
        </Animated.View>
        <Animated.View style={{ transform: [{ scale: zoomAnimation }] }}>
          <TouchableOpacity style={styles.zoomButton} onPress={zoomOut}>
            <Text style={styles.zoomButtonText}>Zoom Out</Text>
          </TouchableOpacity>
        </Animated.View>
      </View>
    </View>
  );
};

const App = () => {
  return (
    <NavigationContainer>
      <Drawer.Navigator
        drawerContent={(props) => <Sidebar {...props} />}
        screenOptions={({ route }) => ({
          headerStyle: styles.headerStyle,
          headerTitleAlign: 'left',
          headerTitle: 'SpillDrill',
          headerTitleStyle: styles.headerTitleStyle,
          headerRight: () => (
            <TouchableOpacity style={styles.alertIcon} onPress={() => {/* Handle alert icon press */}}>
              <Ionicons name="warning-outline" size={24} color="red" />
            </TouchableOpacity>
          ),
        })}
      >
        <Drawer.Screen name="Home" component={HomeScreen} />
        <Drawer.Screen name="Profile" component={Profile} />
        <Drawer.Screen name="Alerts" component={Alerts} />
        <Drawer.Screen name="Report" component={Report} />
        <Drawer.Screen name="Settings" component={Settings} />
        <Drawer.Screen name="OilSpillPrediction" component={OilSpillPrediction} />
      </Drawer.Navigator>
    </NavigationContainer>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  map: {
    ...StyleSheet.absoluteFillObject,
  },
  buttonContainer: {
    position: 'absolute',
    bottom: 50,
    right: 20,
  },
  zoomButton: {
    textAlign: 'center',
    padding: 9,
    backgroundColor: '#007AFF',
    marginBottom: 10,
    borderRadius: 18,
    shadowColor: '#000',
    shadowOffset: { width: 4, height: 2 },
    shadowOpacity: 1,
    shadowRadius: 6,
    elevation: 5,
  },
  zoomButtonText: {
    fontSize: 16,
    color: '#fff',
    fontWeight: 'bold',
  },
  headerStyle: {
    backgroundColor: '#ffffff',
    borderBottomLeftRadius: 15,
    borderBottomRightRadius: 15,
    height: 95,
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 3,
  },
  headerTitleStyle: {
    color: '#007AFF',
    fontSize: 30,
    fontWeight: 'bold',
    paddingLeft: 140,
  },
  alertIcon: {
    marginRight:45,
  },
});

export default App;

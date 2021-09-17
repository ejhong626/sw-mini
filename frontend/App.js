import { StatusBar } from 'expo-status-bar';
import React, { Component } from 'react';
import { StyleSheet, TouchableOpacity, Text, View, Platform } from 'react-native';

import { NavigationContainer, DefaultTheme, DarkTheme } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import LogScreen from './screens/login'; 
import MainScreen from './screens/main';
import RecipeScreen from './screens/recipe';
import ScanScreen from './screens/scan';
import ResultScreen from './screens/result';
import IntakeScreen from './screens/intake';


const Stack = createNativeStackNavigator(); 

const HomeScreen = ({navigation}) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome!</Text>
      <TouchableOpacity
       style={styles.button}
       onPress={() => navigation.navigate("Log In")}
      >
       <Text>Log In</Text>
      </TouchableOpacity>
    </View>
  )
}

const RegisterScreen = ({navigation}) =>{
  return(
    <View style={styles.container}>
      <Text> Registration </Text>
    </View>
  )
}

const App = () =>{
    return (
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen name='Home' component={HomeScreen}/>
          <Stack.Screen name='Log In' component={LogScreen}/>
          <Stack.Screen name='Main' component={MainScreen}/>
          <Stack.Screen name='Recipe' component={RecipeScreen}/>
          <Stack.Screen name='Scan' component={ScanScreen}/>
          <Stack.Screen name='Result' component={ResultScreen}/>
          <Stack.Screen name='Intake' component={IntakeScreen}/>
          
        </Stack.Navigator>
      </NavigationContainer>
    )
  
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: Platform.OS === "android" ? 20:0,
    alignItems: 'center',
    justifyContent: 'center'
  },
  button: {
    alignItems: 'center',
    backgroundColor: '#DDDDDD',
    padding: 10,
    paddingHorizontal: 60,
    marginBottom: 10,
  },
  title: {
    marginTop: 16,
    paddingVertical: 8,
    color: "#20232a",
    textAlign: "center",
    fontSize: 30,
    fontWeight: "bold"
  }
});

export default App;

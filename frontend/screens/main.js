import React, { Component } from 'react';
import { StyleSheet, TouchableOpacity, Text, View, Platform, TextInput } from 'react-native';

import { NavigationContainer, DefaultTheme, DarkTheme } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const MainScreen = ({navigation}) =>{
    return(
      <View style={styles.container}>
        <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Recipe")}
        >
         <Text>Recipe</Text>
        </TouchableOpacity>
        <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Intake")}
        >
         <Text>Daily Intake</Text>
        </TouchableOpacity>
      </View>
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
    padding: 10,
    paddingHorizontal: 60,
    marginBottom: 10,
    borderBottomColor: "red",
    borderBottomWidth: StyleSheet.hairlineWidth
  },
  title: {
    marginTop: 16,
    paddingVertical: 8,
    color: "#20232a",
    textAlign: "center",
    fontSize: 30,
    fontWeight: "bold"
  },
  userInput:{
    flex: 1,
    color: 'C4C4C4',
    fontSize: 10,
  },
  action:{
    flexDirection: 'row',
    paddingBottom: 10,
    marginTop: 10,
  }
});

 export default MainScreen;
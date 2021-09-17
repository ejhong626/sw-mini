import React, { useState } from 'react';
import { StyleSheet, TouchableOpacity, Text, View, Platform, TextInput, Alert } from 'react-native';

import { NavigationContainer, DefaultTheme, DarkTheme } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const LogScreen = ({navigation}) =>{
    const [value, setValue] = useState({
      email: '',
      password: ''
    })

    const onPress = () => {
      console.log(JSON.stringify(value))
      setValue({
        username: '',
        password: ''
      })
      navigation.navigate("Main")
    }

    return(
      <View style={styles.container}>
        <Text style={styles.title}> Hello! </Text>
        <View style={styles.action}>
          <Text> Email </Text>
          <TextInput
            placeholder = 'Email'
            style = {styles.userInput}
            onChangeText={(text) => setValue({ ...value, email: text })}
          />
        </View>
        <View style={styles.action}>
          <Text> Password </Text>
          <TextInput
            placeholder = 'Password'
            style = {styles.userInput}
            onChangeText={(text) => setValue({ ...value, password: text })}
            secureTextEntry = {true}
          />
        </View>
        <TouchableOpacity
          style={styles.button}
          onPress={onPress}>
          <Text>Enter</Text>
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
    alignItems: 'center',
    backgroundColor: '#DDDDDD',
    padding: 5,
    paddingHorizontal: 60,
    marginBottom: 10,
    marginTop: 20
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

 export default LogScreen;


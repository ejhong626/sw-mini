import React, { Component } from 'react';
import { StyleSheet, TouchableOpacity, Text, View, Platform, TextInput } from 'react-native';


export default class ResultScreen extends Component{
    constructor(props){
      super(props); 
      this.result = 0; 
    };
    render(){
      return(
        <View style={styles.container}>
            <Text style={styles.title}>You have taken {this.result} calories!</Text>
        </View>
      )
    }
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
  

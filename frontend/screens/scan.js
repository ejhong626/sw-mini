import React, { useState, Component } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, Platform } from 'react-native';
import { BarCodeScanner } from 'expo-barcode-scanner';

export default function Scanner({ route, navigation: { navigate } }){
    const [hasPermission, setHasPermission] = useState(null);

    useEffect(() => {
      (async () => {
        const { status } = await Camera.requestPermissionsAsync();
        setHasPermission(status === 'granted');
      })();
    }, []);

    const BarCodeScanned = ({ type, data }) => {
      navigation.goBack();
      navigation.state.params.onGoBack({ data });
    };

    if (hasPermission === null) {
      return <Text>Requesting for camera permission</Text>;
    }
    if (hasPermission === false) {
      return <Text>No access to camera</Text>;
    }
    
    return(
      <View style={styles.container}>
      <BarCodeScanner
        onBarCodeScanned={BarCodeScanned}
        style={StyleSheet.camera}
      />   
      </View>
    );
    
};

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
    },
    canmera:{
      flex: 1, 
    }
  });

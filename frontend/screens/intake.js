import React, { useState } from 'react';
import { StyleSheet, TouchableOpacity, Text, View, Platform, TextInput, ActivityIndicator } from 'react-native';

import { Feather } from '@expo/vector-icons';

const IntakeScreen = ({navigation}) =>{
    const [scanned, setScanned] = useState({
        scanned1: false,
        scanned2: false, 
        scanned3: false,
        scanned4: false,
        scanned5: false
    }); 
    const [value, setValue] = useState({
        item1: '',
        barcode1: '',
        item2: '',
        barcode2: '',
        item3: '',
        barcode3: '',
        item4: '',
        barcode4: '',
        item5: '',
        barcode5: ''
        }); 

      const onPress = () => {
        console.log(JSON.stringify(value))
        setValue({
          item1: '',
          barcode1: '',
          item2: '',
          barcode2: '',
          item3: '',
          barcode3: '',
          item4: '',
          barcode4: '',
          item5: '',
          barcode5: ''
        })
        navigation.navigate("Result")
      }

      const refresh = () => {
        setValue({
          recipe_name: '',
          item1: '',
          barcode1: '',
          item2: '',
          barcode2: '',
          item3: '',
          barcode3: '',
          item4: '',
          barcode4: '',
          item5: '',
          barcode5: ''
         })
         setScanned({
          scanned1: false,
          scanned2: false, 
          scanned3: false,
          scanned4: false,
          scanned5: false
         })
      }

      const onGoBack = (data) => {
        if (scanned1){
          setValue({barcode1:{data}});
          setScanned({scanned1:false});
        }
        else if (scanned2){
          setValue({barcode2:{data}});
          setScanned({scanned2:false}); 
        }
        else if (scanned3){
          setValue({barcode3:{data}});
          setScanned({scanned3:false}); 
        }
        else if (scanned4){
          setValue({barcode4:{data}});
          setScanned({scanned4:false}); 
        }
        else if (scanned5){
          setValue({barcode5:{data}});
          setScanned({scanned5:false}); 
        }
    };

      return(
        <View style={styles.container}> 
          <Text style={styles.title}>Daily Intake</Text>  
          <Text style={styles.text}>(Please input the serving values in grams) </Text> 
          <View style={styles.action}>  
              <Text> Item 1  </Text>
              <TextInput 
                  placeholder = 'Serving'
                  style = {styles.userInput}
                  onChangeText={(text) => setValue({ ...value, item1: text })}
              />
              <TouchableOpacity
              style={styles.camera}
              onPress={() => { 
                setScanned({scanned1:true})
                navigation.navigate("Scan", {onGoBack})}}
              >
                  <Feather
                      name='camera'
                      size={10}
                  />
              </TouchableOpacity>
          </View>
          <View style={styles.action}>  
              <Text> Item 2 </Text>
              <TextInput 
                  placeholder = 'Serving'
                  style = {styles.userInput}
                  onChangeText={(text) => setValue({ ...value, item2: text })}
              />
              <TouchableOpacity
              style={styles.camera}
              onPress={() => { 
                setScanned({scanned2:true})
                navigation.navigate("Scan", {onGoBack})}}
              >
                  <Feather
                      name='camera'
                      size={10}
                  />
              </TouchableOpacity>
          </View>
          <View style={styles.action}>  
              <Text> Item 3  </Text>
              <TextInput 
                  placeholder = 'Serving'
                  style = {styles.userInput}
                  onChangeText={(text) => setValue({ ...value, item3: text })}
              />
              <TouchableOpacity
              style={styles.camera}
              onPress={() => { 
                setScanned({scanned3:true})
                navigation.navigate("Scan", {onGoBack})}}
              >
                  <Feather
                      name='camera'
                      size={10}
                  />
              </TouchableOpacity>
          </View>
          <View style={styles.action}>  
              <Text> Item 4  </Text>
              <TextInput 
                  placeholder = 'Serving'
                  style = {styles.userInput}
                  onChangeText={(text) => setValue({ ...value, item4: text })}
              />
              <TouchableOpacity
              style={styles.camera}
              onPress={() => { 
                setScanned({scanned4:true})
                navigation.navigate("Scan", {onGoBack})}}
              >
                  <Feather
                      name='camera'
                      size={10}
                  />
              </TouchableOpacity>
          </View>
          <View style={styles.action}>  
              <Text> Item 5  </Text>
              <TextInput 
                  placeholder = 'Serving'
                  style = {styles.userInput}
                  onChangeText={(text) => setValue({ ...value, item5: text })}
              />
              <TouchableOpacity
              style={styles.camera}
              onPress={() => { 
                setScanned({scanned5:true})
                navigation.navigate("Scan", {onGoBack})}}
              >
                  <Feather
                      name='camera'
                      size={10}
                  />
              </TouchableOpacity>
          </View>
          <View style = {styles.bottom}>
            <TouchableOpacity
              style={styles.button}
              onPress={onPress}>
              <Text>Enter</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={styles.button}
              onPress={refresh}>
              <Text>Refresh</Text>
            </TouchableOpacity>
          </View>
        </View>
      )
    
 };

 const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: Platform.OS === "android" ? 20:0,
    alignItems: 'center',
    justifyContent: 'center'
  },
  bottom:{
    flexDirection: 'row'
  },
  text: {
    paddingBottom: 10
  },
  button: {
    alignItems: 'center',
    backgroundColor: '#DDDDDD',
    borderWidth: 2,
    padding: 5,
    paddingHorizontal: 60,
    marginBottom: 10,
  },
  camera: {
    padding: 10,
    paddingBottom: 10
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

export default IntakeScreen; 

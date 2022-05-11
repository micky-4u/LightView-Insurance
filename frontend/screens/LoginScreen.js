import React, {useState} from 'react'
import { View, Text, StyleSheet, TextInput, Image, TouchableOpacity, Dimensions  } from 'react-native'
import { Ionicons } from '@expo/vector-icons'

import Colors from '../components/Colors'

const width = Dimensions.get("window").width

export default function Login({navigation}) {
  return (
    <View style={styles.container}>
      <Image source={require("../assets/images/logo.png")} style={styles.logo}/>
      <Text style={styles.loginText}>Log into your account</Text>


      <Text style={styles.mainInputText}>Email</Text>
      <TextInput 
      placeholder='Email address'
      style={styles.textInput}
      />

      <Text style={styles.mainInputText}>Password</Text>
      <View>
      <TextInput 
      placeholder='Password'
      style={styles.textInput}
      />
      <TouchableOpacity>
        <Ionicons name='ios-eye-off-outline' size={24}/>
      </TouchableOpacity>
      </View>
 
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    // alignItems: 'center',
    paddingHorizontal: 20,
  },
  logo: {
    width: width*0.15,
    height: width*0.15,
    marginBottom: 115,
    alignSelf: 'center'
  },
  loginText: {
    fontFamily: 'Medium',
    fontSize: 18
  }
})
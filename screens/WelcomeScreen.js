import React from 'react'
import { View, Text, StyleSheet, Image, TouchableOpacity, Dimensions } from 'react-native'

import Colors from '../components/Colors'

const width = Dimensions.get("window").width

export default function Welcome({navigation}) {
  return (
    <View style={styles.container}>
      <Image source={require("../assets/images/logo.png")} style={styles.logo}/>

      <Image source={require("../assets/images/service.png")} style={styles.svg}/>
      
      <Text style={styles.mainText}>Begin your Insurance journey</Text>

      <Text style={styles.subText}>Lorem ipsum dolor sit amet, consectetur</Text>

      <TouchableOpacity activeOpacity={0.7} style={styles.login} onPress={() => navigation.navigate("Login")}>
        <Text style={styles.loginText}>Login</Text>
      </TouchableOpacity>

      <TouchableOpacity activeOpacity={0.7} style={styles.signup} onPress={() => navigation.navigate("Signup")}>
        <Text style={styles.signupText}>Sign up</Text>
      </TouchableOpacity>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 20
  },
  logo: {
    width: width*0.15,
    height: width*0.15
  },
  svg: {
    width: width*0.75,
    height: width*0.75,
    resizeMode: 'contain',
    marginTop: 40,
    marginBottom: 20
  },
  mainText: {
    fontFamily: 'Semibold',
    fontSize: 26,
    textAlign: 'center',
    marginBottom: 10
  },
  subText: {
    fontFamily: 'Regular',
    fontSize: 16,
    color: '#000',
    opacity: 0.6,
    marginBottom: 30
  },
  login: {
    width: "100%",
    height: 55,
    backgroundColor: Colors.main,
    borderRadius: 5,
    marginBottom: 20,
    shadowColor: Colors.main,
    alignItems: "center",
    justifyContent: "center",
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  loginText: {
    fontFamily: "Semibold",
    fontSize: 16,
    color: Colors.white
  },
  signup: {
    width: "100%",
    height: 55,
    borderWidth: 2,
    borderColor: Colors.main,
    backgroundColor: Colors.white,
    borderRadius: 5,
    alignItems: "center",
    justifyContent: "center",
  },
  signupText: {
    fontFamily: "Semibold",
    fontSize: 16,
    color: Colors.main
  }
})
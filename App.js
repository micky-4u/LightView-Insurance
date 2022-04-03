//import 'react-native-gesture-handler';

import { StyleSheet, Text, View } from 'react-native';

import { useFonts } from 'expo-font';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import Welcome from "./screens/WelcomeScreen"
import Signup from "./screens/SignupScreen"
import Login from "./screens/LoginScreen"

const Stack = createNativeStackNavigator()

export default function App() {
  const [loaded] = useFonts({
    Semibold: require('./assets/fonts/Poppins-SemiBold.ttf'),
    Medium: require('./assets/fonts/Poppins-Medium.ttf'),
    Regular: require('./assets/fonts/Poppins-Regular.ttf'),
    Light: require('./assets/fonts/Poppins-Light.ttf'),
  });

  if (!loaded) {
    return null;
  }

  return (
    <NavigationContainer>
      <Stack.Navigator 
      screenOptions={{headerShown: false}}
      initialRouteName="Welcome"
      >
        <Stack.Screen name="Welcome" component={Welcome}/>
        <Stack.Screen name="Login" component={Login}/>
        <Stack.Screen name="Signup" component={Signup}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

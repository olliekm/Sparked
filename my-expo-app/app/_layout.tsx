import { useFonts } from 'expo-font';
import { Stack } from 'expo-router';
import { useEffect } from 'react';
import { View } from 'react-native';

export default function RootLayout() {


  return (
    <Stack
      screenOptions={{
          // Hide the header for all other routes.
          headerShown: false, 
        }}>
        <Stack.Screen name="index" options={{ headerShown: false }} />
    </Stack>
  );
}

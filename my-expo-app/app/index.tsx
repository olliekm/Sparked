import React from 'react'
import { View, Text } from 'react-native'
import { Link } from 'expo-router'

import '../global.css'
import { ScreenContent } from 'components/ScreenContent'

export default function index() {
  return (
    <>
        <ScreenContent>
            <View className='h-16 w-16 bg-white pt-20'>
                <Text className='text-white'>YO</Text>
                <Link href={'/workout'}>
                    workout
                </Link>
            </View>
        </ScreenContent>
    </>
  )
}
import React from 'react'
import { View, Text } from 'react-native'
import { Link } from 'expo-router'

import '../global.css'
import { ScreenContent } from 'components/ScreenContent'

export default function index() {
  return (
    <>
        <ScreenContent>
            <View className='pt-20'>
                <Text className='text-white'>YO</Text>
                <Link href={'/workout'}>
                    workout
                </Link>
                <Link href={'/splash'}>
                    splash
                </Link>
                <Link href={'/home'}>
                    home
                </Link>
            </View>
        </ScreenContent>
    </>
  )
}
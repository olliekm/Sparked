import { Text, View } from 'react-native'
import React, { Component } from 'react'
import { Link } from 'expo-router'

export class index extends Component {
  render() {
    return (
      <View className='h-screen bg-primary pt-10'>
        <View className='p-8'>
            <Text className='text-secondary font-bold text-3xl'>Hello,</Text>
            <Text className='text-secondary font-bold text-6xl'>Oliver</Text>
        </View>
        <View className='w-full flex flex-row h-80'>
            <View className='w-1/2 h-full border-y-2 border-secondary'></View>
            <View className='w-1/2 flex flex-col relative border-l-2 border-y border-secondary'>
                <View className=' h-1/2 border-b-2 border-secondary flex justify-center items-center'>
                    <Text className='text-2xl font-bold text-secondary'>Stats</Text>
                </View>
                <View className=' h-1/2 '></View>
            </View>
        </View>
        <Link href={'/workout'} className="absolute bottom-8 self-center" >
            <View className='p-6 px-12 font-bold text-center text-xl bg-accent2 text-primary rounded-full'>
                <Text className='text-white text-xl font-bold'>Start Workout ✨</Text>
            </View>
        </Link>
      </View>
    )
  }
}

export default index
import { Text, View, TouchableOpacity, ImageBackground } from 'react-native'
import React, { Component } from 'react'
import { Link } from 'expo-router'
import Lightning from 'components/LightningWhiteLogo';

const image = {uri: 'https://images.unsplash.com/photo-1600340669742-2d181b86ca73?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fHNsYXRlfGVufDB8fDB8fHww'};

export class index extends Component {
  render() {
    return (
      <ImageBackground source={image} className='h-screen'>
        <View className='h-screen bg-[#000]/80 flex text-secondary'>
            <View className='absolute left-0 rotate-[30deg]'>
              <Lightning opacity={0.1} width={1000} height={1000}/>
            </View>
            <View className='w-full flex justify-center items-center pt-20'>
              <View className='flex flex-row items-center'>
                <Text className='text-secondary font-bold text-lg'>Sparked</Text>
              <Lightning height={16} width={16}/>

              </View>
            </View>
            <View className='absolute bottom-0 w-full p-8 pb-16'>
                <View className='w-full pb-8'>
                  <Text className='text-secondary text-3xl font-bold text-center pb-2'>Welcome to Sparked</Text>
                  <Text className='text-secondary text-center'>Your new favourite climbing log.</Text>

                </View>
                <Link href="/auth/register" className='p-6 w-full font-bold text-center text-xl bg-accent2 text-primary rounded-full'>
                  Create new account
                </Link>
                <Link href="/auth/login" className='p-6 mt-4 w-full font-bold text-center text-xl underline text-secondary rounded-full'>
                  Log into existing account
                </Link>
            </View>
        </View>
      </ImageBackground>

    )
  }
}

export default index
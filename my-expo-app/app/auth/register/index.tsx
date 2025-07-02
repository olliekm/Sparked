import { Text, TextInput, View, TouchableOpacity } from 'react-native'
import React, { Component } from 'react'

export class index extends Component {
  render() {
    return (
      <View className='h-screen bg-primary pt-20 flex flex-col justify-center items-center'>
        <View>
            <Text className='text-secondary text-3xl font-bold pb-2'>Register</Text>
            <View className='w-64'>
                <TextInput placeholder='EMAIL' className='bg-secondary/10 text-secondary p-4 rounded-full w-full'/>
                <TextInput placeholder='PASSWORD' className='bg-secondary/10 text-secondary p-4 rounded-full w-full'/>
                <TextInput placeholder='USERNAME' className='bg-secondary/10 text-secondary p-4 rounded-full w-full'/>
                <TouchableOpacity className='bg-accent2 text-xl font-bold p-4 rounded-full'> 
                    <Text className='text-center'>Register</Text>
                </TouchableOpacity>
            </View>
        </View>
      </View>
    )
  }
}

export default index
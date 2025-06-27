import { Text, View } from 'react-native'
import React, { Component } from 'react'

export class index extends Component {
  render() {
    return (
      <View className='h-screen bg-primary flex text-secondary justify-center items-center'>
        <Text className='font-bold text-secondary text-4xl'>Sparked</Text>
      </View>
    )
  }
}

export default index
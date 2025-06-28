import { ScreenContent } from 'components/ScreenContent';
import { StatusBar } from 'expo-status-bar';
import { Text, TextInput, TouchableOpacity, View } from 'react-native';
import { useState } from 'react';
import { Link } from 'expo-router';


import '../../global.css';

export default function App() {
  const [journal, setJournal] = useState("")
  const [loading, setLoading] = useState(false);
  const saveJournal = async () => {
    setLoading(true)
    try {
      const response = await fetch('http://127.0.0.1:8000/prompt', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          journal: journal,
        }),
      });
      const json = await response.json()
      console.log("WHAT")
      console.log(json)
    } catch (error) {
      console.error("Error saving journal:", error);
    }

    setJournal(""); // Clear the input after saving
    setLoading(false);
  }
  return (
    <>
      <ScreenContent>
      <View className='w-full h-auto px-4 flex flex-row items-end justify-between text-secondary'>
        <Text className='text-secondary text-3xl font-bold px-4'>Sparked.</Text>
        <Text className='text-secondary text-xl px-4'>Your workout journal</Text>
      </View>
        {
          loading ? 
          <View className='w-full h-screen absolute z-10 bg-indigo-900/80 items-center justify-center'>
            <Text className='text-white text-2xl'>Saving your journal...</Text>
          </View> 
          : null
        }
        <TextInput 
            keyboardAppearance='dark'
            onChangeText={journal => setJournal(journal)} 
            value={journal}
            className='placeholder:text-gray-400  text-secondary text-start text-3xl p-4 h-screen '
            editable
            multiline
            numberOfLines={30}
            maxLength={1000}
            placeholder='Write your journal here ✏️...'
            ></TextInput>
          <TouchableOpacity disabled={loading} onPress={saveJournal} className='absolute z-10 bottom-0 right-0 font-bold bg-accent p-2 rounded-lg h-auto w-auto m-10'>
            <Text className='text-lg px-4'>DONE</Text>
          </TouchableOpacity>
          <Link href="/" className='absolute bottom-0 left-0 m-10'>
          home
          </Link>
      </ScreenContent>
      <StatusBar style="auto" />
    </>
  );
}

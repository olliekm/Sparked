import { Text, View } from 'react-native';

import { EditScreenInfo } from './EditScreenInfo';

type ScreenContentProps = {
  title: string;
  path: string;
  children?: React.ReactNode;
};

export const ScreenContent = ({ title, path, children }: ScreenContentProps) => {
  return (
    <View className='bg-gray-800 w-full h-screen text-white pt-20'>
      <View className='w-full h-auto px-4 flex flex-row items-end justify-between'>
        <Text className='text-white text-3xl font-bold px-4'>ogi.</Text>
        <Text className='text-white text-xl px-4'>Your workout journal</Text>
      </View>
      {/* <Text className={styles.title}>{title}</Text> */}
      {children}
    </View>
  );
};

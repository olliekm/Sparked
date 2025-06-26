import { Text, View } from 'react-native';

import { EditScreenInfo } from './EditScreenInfo';

type ScreenContentProps = {
  children?: React.ReactNode;
};

export const ScreenContent = ({ children }: ScreenContentProps) => {
  return (
    <View className='bg-gray-800 w-full h-screen text-white pt-20'>

      {/* <Text className={styles.title}>{title}</Text> */}
      {children}
    </View>
  );
};

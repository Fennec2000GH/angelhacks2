import Header from '../Header';
import Body from '../Body';
import { ChakraProvider, Flex, VStack } from '@chakra-ui/react';

export default function App(){
    return(
        <VStack>
            <Header />
            <Body />
        </VStack>
    );
}
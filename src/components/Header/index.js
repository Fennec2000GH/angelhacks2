import { Flex, Heading } from "@chakra-ui/react";

export default function Header(){
    return (
        <Flex
            justifyContent="center"
        >
        <Heading as={"h1"}>Zusammenfassung</Heading>
        </Flex>
    )
}
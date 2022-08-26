pragma solidity >=0.8.13 <0.9.0;

contract HODL_GEN {

    function collision_troll(string memory _text, string memory _anotherText)
        public
        pure
        returns (bytes32)
    {
        return keccak256(abi.encodePacked(_text, _anotherText));
    }

    function hasher(string memory _text) public pure returns (bytes32) {
        return keccak256(abi.encode(_text));
    }
}

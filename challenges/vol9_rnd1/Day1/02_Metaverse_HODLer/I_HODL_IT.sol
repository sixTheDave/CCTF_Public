contract I_HODL_IT {
    bytes32 public val = 0xe1dbfec2e4b2dea9b7199c38ab5a74ad5d186373c2c9c3b8a075da831e652189;

    function I_HODL_THE_FLAG(string memory _flag) public view returns (bool) {
        return keccak256(abi.encodePacked(_flag)) == val;
    }
}

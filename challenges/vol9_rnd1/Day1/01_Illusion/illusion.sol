// SPDX-License-Identifier: MIT
pragma solidity = 0.8.16;

contract MagikTrik {
    constructor (bytes memory x) public {
        assembly{
            return (0xc0, 0x19e)
        }
    }
    
    function flag() public returns (string memory) {
        return "CCTF{0x2311157248adee133b378f46b30050bb4c7508e6bc9043eae5e6566f5fe8595e}";
    }
}

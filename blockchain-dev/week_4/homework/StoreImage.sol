// SPDX-License-Identifier: MIT

// pragma solidity >=0.6.0 <0.9.0;
contract DataContract {
    // Declaring state variables 
    string public size;
    string public img;
    
    // Defining public function  
    // that sets the value of  
    // the state variable 
    function set(string calldata x, string calldata y) public
    { 
        size = x;
        img = y;
    
    } 
        
    // Defining function to 
    // print the sum of 
    // state variables 
    function get_size( 
    ) public view returns (string memory) { 
        return size; 
    } 

    function get_image( 
    ) public view returns (string memory) { 
        return img; 
    }
}





// contract DataContract {

//     address public owner;
//     string[] public data;

//     // Constructor
//     constructor() public {
//         owner = msg.sender;
//     }

// function putData(string  memory _d) public {
//     data.push(_d);
// }

// }




// contract StoreImage {

//     string img;

//     // This is a comment!
//     struct Image {
//         string image;
//         string size;
//     }

//     Image[] public image;
//     mapping(string => string) public picture;

//     function store(string _img) public {
//         img = _img;
//     }
    
//     function retrieve() public view returns (string){
//         return img;
//     }

//     function addPerson(string memory _size, string _img) public {
//         image.push(Image(_img, _size));
//         picture[_size] = _img;
//     }
// }
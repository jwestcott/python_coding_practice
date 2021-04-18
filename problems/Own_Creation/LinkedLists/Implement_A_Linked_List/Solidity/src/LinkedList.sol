// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.6.0 <0.9.0;

contract LinkedList {
    
    uint256 public head; //change to bytes
    uint256 public prevNode;
    bool public headExist = false;
    
    //prevNode could be an array of nodes but that would get quite expensive so a few downsides when implementing huge getListState
    //can use struct as struct Node with indexing so that we can count how many items in the list as can't iterate over mappings
    
    mapping(uint256 => mapping(bool => uint256)) linkedList;
    
    event LinkedList(uint256 head, uint256 node);
    event AppendList(uint256 head, uint256 prevNode, uint256 newNode);
    
    function initializeList(uint256 _head, uint256 _node) public returns (bool, uint256, uint256){
        headExist = true;
        linkedList[_head][headExist] = _node;
        head = _head;
        prevNode = _node;
        
        emit LinkedList(head, linkedList[_head][headExist]);
        
        return (headExist, _head, linkedList[_head][headExist]);//linkedList[newHead][headExist];
        
    }
    
    function append(uint256 _node) public returns (uint256){
        if (head != _node && prevNode != _node) {
            linkedList[prevNode][headExist] = _node;
            emit AppendList(head, prevNode, linkedList[prevNode][headExist]);
        }
        return linkedList[prevNode][headExist];
    }
    
    function getListState() public returns (bool, uint256, uint256) {
        return (headExist, head, prevNode);
    }
    
}
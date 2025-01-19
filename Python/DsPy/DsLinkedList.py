import copy

#Py: 抽象類別必須指定 metaClass 來繼承 abc.ABCMeta class
from abc import ABCMeta, abstractmethod

class DsSingleLinkedListNode:
    """ A Single Linked List Node Implements.
    
    Attributes
    ----------
    data: Any
        The data of the node
    next: DsSingleLinkedListNode
        A Link For linking to next node

    Methods
    -------
    print_node(self)
        The function is to print the data of the node
    """

    def __init__(self, data=0, next=None):
        """ The initialized function for a new Single Linked List Node.

        Parameters
        ----------
        data: any
            The data of the node, by default is NULL.
        next: DsSingleLinkedListNode
            A Link For linking to next node, by default is NULL.
        """

        self.data = data
        self.next = next

    #Py: self.__repr__ : print object with string format we would give
    def __repr__(self) -> str:
        s = f"DsSingleLinkedListNode.data = {self.data}, next to "
        n = "NULL" if (not self.next) else str(self.next.data)
        return s+n

    def print_node(self):
        """ Print the data of the Single Linked List Node. """
        print(f"data = {self.data}")

#Py: Define a Abstract Class
class DsLinkedList(metaclass=ABCMeta):
    """An abstract Linked List class to be the base of all types of linked list. 

    Attributes
    ----------
    Head: DsSingleLinkedListNode
        A progerty, The head node of the Linked List.
    Tail: DsSingleLinkedListNode
        A progerty, The tail node of the Linked List.

    Methods
    -------
    getListLength()
        Return the Length of the Linked List.
    insertFrontNode(NewNode)
        @abstractmethod add a new Single Linked List Node into Head.
    insertNodeAfterIndex(NewNode, index:int)
       @abstractmethod Insert a new Single Linked List Node into Linked List after the node with the index.
    appendNode(NewNode)
       @abstractmethod Insert a new Single Linked List Node into the tail of the linked list.
    deleteFrontNode()
       @abstractmethod Delete the headed Single Linked List Node of the linked list.
    deleteNodeByIndex(index:int)
       @abstractmethod Delete a Single Linked List Node with its index.
    deleteLasteNode()
       @abstractmethod Delete the last Single Linked List Node.
    deleteNode(node)
       @abstractmethod Delete a Single Linked List Node.
    """
    
    def __init__(self):
        self.__head = None #Py: Private Member
        self.__tail = None
        self.__number = 0

    #Python: Use Property can produce a getter of the private member in a class
    #        with @property
    #             def <Gettor Name>(self): return self.<private member name>
    @property
    def Head(self): return self.__head
    #Python: after defining a getter for a private member, we can use the getter name to generate a setter
    #        with @<Getter Name>.setter
    #             def <Gettor Name>(self, value): set <private member name> with value
    @Head.setter
    def Head(self, value): self.__head = value

    @property
    def Tail(self): return self.__tail
    @Tail.setter
    def Tail(self, value): self.__tail = value

    def getListLength(self): 
        """ Return the Length of the Linked List.

        Returns
        -------
        int:
            The Integer to indicate the length of the Linked List
        """
        return self.__number

    #1 Tips: abstract insert node functions
    #Py: @abc.abstrctmethod - declare a method is an abstract method needs be overwritten by sub class
    #    if there are multiple properties in a function, the  @abc.abstrctmethod must be in the deepest loop
    @abstractmethod
    def insertFrontNode(self, NewNode): pass
    @abstractmethod
    def insertNodeAfterIndex(self, NewNode, index:int): pass
    @abstractmethod
    def appendNode(self, NewNode): pass
    #1 End
    
    #2 Tips: abstract delete node functions
    @abstractmethod
    def deleteFrontNode(self): pass
    @abstractmethod
    def deleteNodeByIndex(self, index): pass
    @abstractmethod
    def deleteLastNode(self): pass
    @abstractmethod
    def deleteNode(self, node): pass
    #2 End

class DsSingleLinkedList(DsLinkedList):
    """Single Linked List class for Data Structure Practice, It is derived by the DsLinkedList abstract class.

    Attributes
    ----------

    Methods
    -------
    """

    #Py: Call super init function for the instance construstor
    def __init__(self): super().__init__()
    
    def insertFrontNode(self, NewNode:DsSingleLinkedListNode):
        """ add a new Single Linked List Node into Head.

        Parameters
        ----------
        NewNode: DsSingleLinkedListNode
            The Inserting Single Linked List Node
        
        Returns
        -------
        bool
            return a boolean Result for the inserting action.
        """

        print(f"[insertFrontNode] Try to Insert a New Node {NewNode.data} into the Head")
        if not self.Head:
            self.Head = NewNode
            self.Tail = NewNode
        else:
            NewNode.next = self.Head
            self.Head = NewNode
            print(f"  - New Head after Inserting a Node into Head: {self.Head.data}")

        #Py: 子類別如何存取父類別的私有成員? 對象名._类名__私有成员
        #    子类调用父类私有数据域：self._父类名+私有数据名
        #    子类调用父类私有方法：self._父类名+私有方法名
        self._DsLinkedList__number += 1

        print(f"::Inserted a New Node into Head: {NewNode.data}")
        return True
    
    def insertNodeAfterIndex(self, NewNode:DsSingleLinkedListNode, index:int):
        """ Insert a new Single Linked List Node into Linked List after the node with the index.

        Parameters
        ----------
        NewNode: DsSingleLinkedListNode
            The Inserting Single Linked List Node.
        index: int
            The location we would insert node into, its range starts from 1 to the length of the list.

        Returns
        -------
        bool
            return a boolean Result for the inserting action.
        """

        print(f"[insertNodeAfterIndex] Try to Insert a New Node {NewNode.data} after Index: {index}")
        if not index: 
            # Py: 也可以用 raise Exception("Error: index must be equal to or exceeding 1") 故意引發錯誤
            print("  - [InvalidError]: index must be equal to or exceeding 1")
            return False
        if (index==1 or self._DsLinkedList__number==0): 
            self.insertFrontNode(NewNode)
            return True
        if index > self._DsLinkedList__number: 
            print(f"  - [InvalidError]: index is over list boundry {self._DsLinkedList__number}")
            return False

        current_node = self.Head

        for i in range(1, self._DsLinkedList__number+1):
            if i < index: 
                #print("i = %d"%i)
                current_node = current_node.next
                continue
            break

        if index == self._DsLinkedList__number: 
            self.Tail = NewNode
            print(f"  - New Tail after Inserting a Node by Index {index}: {self.Tail.data}")

        NewNode.next = current_node.next
        current_node.next = NewNode
        self._DsLinkedList__number += 1

        print(f"::Inserted a New Node by Index: {NewNode.data}")
        return True
    
    def appendNode(self, NewNode:DsSingleLinkedListNode):
        """ Insert a new Single Linked List Node into the tail of the linked list.

        Parameters
        ----------
        NewNode: DsSingleLinkedListNode
            The Inserting Single Linked List Node.
        """

        print(f"[appendNode] Try to append a Node: {NewNode.data}")
        if not self.Head:
            self.Head = NewNode
            self.Tail = NewNode
        else:
            self.Tail.next = NewNode   #Tips: Extend List to New Node
            self.Tail = self.Tail.next #Tips: Update List Tail Node 
        print(f"  - New Tail after appending a Node: {self.Tail.data}")
        print(f"::Appended a New Node: {NewNode.data}")
        #print("head = %s, tail = %s"%(self.Head.data, self.tail.data))
        self._DsLinkedList__number += 1
    
    def deleteFrontNode(self):
        """ Delete the headed Single Linked List Node of the linked list.
        
        Returns
        -------
        bool
            return True or False to indicate the deleted result.
        """

        print("[deleteFrontNode] Try to delete the head node.")
        if not self.Head: 
            print("[DeleteError]: There is no node can be deleted.")
            return False
        else:
            del_node = self.Head
            self.Head = self.Head.next
            del_node.next = None
            self._DsLinkedList__number = self._DsLinkedList__number - 1
            print(f"  - New Head after deleting Node: {self.Head.data}") if self.Head else print("New Head is Null.")
            print(f"::The Head Node {del_node.data} is deleted.")
            del del_node
            return True
    
    def deleteNodeByIndex(self, index):
        """ Delete a Single Linked List Node with its index.

        Parameters
        ----------
        index: int
            The location we would delete node from, its range starts from 1 to the length of the list.

        Returns
        -------
        bool
            return True or False to indicate the deleted result.
        """

        print("[deleteNodeByIndex] Try to delete a Node at Index %d, The List Length is %d"%(index, self._DsLinkedList__number))
        if not self.Head: print("  - [DeleteError]: There is no node can be deleted."); return False
        if index == 0 or index > self._DsLinkedList__number : 
            print("  - [InvalidError]: Invalid index, index must be between 1 and list-length."); return False
        if index == 1 : self.deleteFrontNode(); return True
        
        del_node = self.Head
        pre_node = None
        for i in range(1, self._DsLinkedList__number):
            if i < index:
                pre_node = del_node
                del_node = del_node.next
                continue
            #print("deleteNodeByIndex.i=%d"%i)
            break
        pre_node.next = del_node.next
        del_node.next = None
        if index == self._DsLinkedList__number: 
            self.Tail = pre_node
            print(f"  - New Tail after deleting Node: {self.Tail.data}")
        del del_node
        self._DsLinkedList__number -= 1
        print(f"::The Index {index} Node is deleted.")
        return True
    
    def deleteLastNode(self): 
        """ Delete the last Single Linked List Node.

        Returns
        -------
        bool
            return True or False to indicate the deleted result.
        """

        print("[deleteLastNode] Try to delete the Tail node.")
        if not self.Head: 
            print("  - [DeleteError]: There is no node can be deleted.")
            return False
        else:
            target = self.Tail.data
            #self.deleteNodeByIndex(self._DsLinkedList__number)
            self.deleteNode(self.Tail)
            print(f"  - New Tail after deleting Node: {self.Tail.data}") if self.Head else print("  - New Tail is Null.")
            print(f"::The Tail Node {target} is deleted.")

        return True

    def deleteNode(self, node:DsSingleLinkedListNode):
        """ Delete a Single Linked List Node.

        Parameters
        ----------
        node: DsSingleLinkedListNode
            The Single Linked List Node we would delete.

        Returns
        -------
        bool
            return True or False to indicate the deleted result.
        """

        target = node.data
        current_node = self.Head
        pre_node = None

        print("[deleteNode] Try to delete a Node: %d"%(target))

        while (current_node):
            if self._DsLinkedList__number == 1:
                print(f"  - The Only Node {current_node.data} will be deleted.")
                del current_node
                self.Head = None
                self.Tail = None
                break
            if (current_node.data != target):
                #1 Tips: move to next node 
                pre_node = current_node
                current_node = current_node.next
                if not current_node: 
                    print("  - [DeleteError]: Delete Node Failed due to not found")
                    return False
                #1 End
            else:
                #2 Tips: found a deleting node and do delete
                pre_node.next = current_node.next #Tips: pre_node links to the node after deleted node
                current_node.next = None
                if not pre_node.next: 
                    print(f"  - The Tail Node {current_node.data} will be deleted.")
                    self.Tail = pre_node #Tips: setup new Tail node
                del current_node
                #2 End
                break

        self._DsLinkedList__number -= 1
        print(f"::The Node {target} is deleted.")

        return True

    def deleteMatchedNodes(self, node:DsSingleLinkedListNode):
        """ Delete all the Single Linked List Nodes with the same data.

        Parameters
        ----------
        node: DsSingleLinkedListNode
            All of the Single Linked List Nodes with the same data we would delete in the linked list.

        Returns
        -------
        int
            return a integer to indicate the deleted-nodes number.
        """

        target = node.data
        del_number = 0
        current_node = self.Head
        pre_node = None

        print("[deleteMatchedNodes] Try to delete all matched Nodes: %d"%(target))
        while (current_node):
            if (current_node.data != target):
                #1 Tips: move to next node 
                pre_node = current_node
                current_node = current_node.next
                #1 End
            else:
                #2 Tips: found a deleting node and do delete
                if current_node == self.Head:
                    current_node = current_node.next
                    self.deleteFrontNode()
                else:
                    pre_node.next = current_node.next #Tips: pre_node links to the node after deleted node
                    current_node.next = None
                    current_node = pre_node.next #Tips: next current node is after the deleted node
                    # Debug: if current_node: print("Debug: New current.data = %d\n"%current_node.data)
                #2 End

                self._DsLinkedList__number -= 1
                del_number += 1
                #print("Deleted %d matched nodes so far"%(del_number))

        print("::Deleted %d matched nodes."%(del_number))
        return del_number
    
    def visit(self):
        """ Visit the Single Linked List. 
        
        Returns
        -------
        int visit_nodes_num
            return a integer to indicate the visited-nodes number.
        """

        s = "<< "
        visit_nodes_num = 0
        node = self.Head
        while (node):
            visit_nodes_num += 1
            s = (s+str(node.data)+" -> ") if node.next else s+str(node.data)
            node = node.next
        #print(f"[Visit] LinkedList Nodes Number: {len}")
        s += " >>"
        print(s)

        return visit_nodes_num

class DsLinkedListHelper:
    """ The common functions for DsLinkedList calss. """
    def __init__(self): pass

    @staticmethod
    def reverseList(list:DsSingleLinkedList):
        """ Reverse a DsLinkedList.

        Parameters
        ----------
        list: DsSingleLinkedList
            A Single Linked List we would reverse

        """

        if list.getListLength() <= 1 : 
            print("[No Reverse] This is an Empty or 1-node list, so it do not be reversed")
            return False
        
        #Tips: the moved rounds of the right_node, the max round = List.Length+1 (if start from 1)
        round = 1

        #1. Tips: Major Algorithm
        #Tips: right_node start from the Head, it will keep moving to tail.next = NULL, 
        #      the node follows it (reverse_node) will be reversed.
        right_node = list.Head
        #Tips: follow right_node to reverse
        reverse_node = None
        #Tips: follow reverse_node so that reverse_node can reverse next link to it
        reverse_next_node = None

        while(right_node):
            #2. Tips: main reverse process
            reverse_next_node = reverse_node
            reverse_node = right_node
            right_node = right_node.next

            #Tips: Reverse the link of the current reversed node
            reverse_node.next = reverse_next_node
            #2. End

            if round == 1: list.Tail = reverse_node
            round += 1
        list.Head = reverse_node
        #1. End
        list.visit()

        return True


if __name__ == "__main__":

    link_list1 = DsSingleLinkedList()
    link_list1.appendNode(DsSingleLinkedListNode(100))
    link_list1.appendNode(DsSingleLinkedListNode(200))
    link_list1.appendNode(DsSingleLinkedListNode(300))
    link_list1.appendNode(DsSingleLinkedListNode(400))
    link_list1.appendNode(DsSingleLinkedListNode(500))
    link_list1.appendNode(DsSingleLinkedListNode(600))
    link_list1.appendNode(DsSingleLinkedListNode(700))

    #Py: We can use copy.deepcopy to copy an object deeply
    link_list2 = copy.deepcopy(link_list1)

    print("Linked List1: ")
    link_list1.visit()
    print("After List1 Reverse: ")
    DsLinkedListHelper.reverseList(link_list1)
    print("List2 Copied Linked List1: ")
    link_list2.visit()




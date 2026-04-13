package main

import "fmt"

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}
	for node := head; node != nil; node = node.Next.Next {
		node.Next = &Node{Val: node.Val, Next: node.Next}
	}
	for node := head; node != nil; node = node.Next.Next {
		if node.Random != nil {
			node.Next.Random = node.Random.Next
		}
	}
	headNew := head.Next
	for node := head; node != nil; node = node.Next {
		nodeNew := node.Next
		node.Next = node.Next.Next
		if nodeNew.Next != nil {
			nodeNew.Next = nodeNew.Next.Next
		}
	}
	return headNew
}

func printList(name string, head *Node) {
	fmt.Println(name)
	for node := head; node != nil; node = node.Next {
		randomVal := "nil"
		if node.Random != nil {
			randomVal = fmt.Sprintf("%d", node.Random.Val)
		}
		fmt.Printf("Val=%d Random=%s\n", node.Val, randomVal)
	}
	fmt.Println()
}

func main() {
	node1 := &Node{Val: 7}
	node2 := &Node{Val: 13}
	node3 := &Node{Val: 11}
	node4 := &Node{Val: 10}
	node5 := &Node{Val: 1}

	node1.Next = node2
	node2.Next = node3
	node3.Next = node4
	node4.Next = node5

	node2.Random = node1
	node3.Random = node5
	node4.Random = node3
	node5.Random = node1

	fmt.Println("复制前：")
	printList("原链表", node1)

	copyHead := copyRandomList(node1)

	fmt.Println("复制后：")
	printList("原链表", node1)
	printList("新链表", copyHead)

	node1.Val = 100
	node3.Random = node1

	fmt.Println("修改原链表后：")
	printList("原链表", node1)
	printList("新链表（保持不变，说明是深拷贝）", copyHead)
}

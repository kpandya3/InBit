# Construct binary tree given inorder and preorder traversals

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def __str__(self):
		return " [ " + str(self.val) + " : " + self.left.__str__() + self.right.__str__() + " ] "

def ConstructBinTree(preorder, inorder):
	if not inorder:
		return None
	root = TreeNode(preorder[0])
	rootPos = inorder.index(preorder[0])
	root.left = ConstructBinTree(preorder[1 : 1 + rootPos], inorder[ : rootPos])
	root.right = ConstructBinTree(preorder[rootPos + 1 : ], inorder[rootPos + 1 : ])
	return root

inorder_list = [4,10,3,1,7,11,8,2]
preorder_list = [7,10,4,3,1,2,8,11]

print(ConstructBinTree(preorder_list, inorder_list))

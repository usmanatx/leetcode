import json

class Node:
   def __init__(self, val=0):
      self.right = ''
      self.left = ''
      self.value = val


class Tree(Node):

   def addNode(self, tree, node, duplicates):
      if not tree:
         tree = node
      elif tree.value > node.value:
         if tree.left:
            tree.left = self.addNode(tree.left, node, duplicates)
         else:
            tree.left = node
      elif tree.value < node.value:
         if tree.right:
            tree.right = self.addNode(tree.right, node, duplicates)
         else:
            tree.right = node
      elif tree.value == node.value:
         duplicates.append(node.value)

      return tree



def buildTree():
   arr = [14, 15, 4, 9, 7, 18, 3, 5, 16, 20,4,17, 9, 14, 5]
   tree = Tree()
   duplicates = []

   for v in arr:
      node = Node(v)
      tree = tree.addNode(tree, node, duplicates)


   s = json.dumps(tree.__dict__, default=serialize)
   print(s)
   print(duplicates)


def serialize(obj):
    return obj.__dict__


if __name__ == '__main__':
   buildTree()

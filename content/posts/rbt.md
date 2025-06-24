---
title: 红黑树(C++)
categories:
- Algorithm and Data Structure
date: "2020-11-08"
tags:
- Algorithm
- Data Structure
- Red-Black Tree	
---

## 红黑树(C++)

### 红黑树性质

+ 每个节点只能是红色或者黑色

+ 根节点是黑色

+ 叶子节点是黑色

+ 红色节点的子节点必须是黑色

+ 任一节点到其子树叶子节点的所有简单路径具有相同数量的黑色节点

  

### 插入

共6种情况，其中33对称，实际上就3种

### 删除

共8种情况，其中44对称，实际上就4种


### 代码实现
```cpp
#include <algorithm>
#include <iostream>

using namespace std;
enum Color {
    RED, BLACK
};

template<typename T>
class Node {
public:
    Node *parent, *left, *right;
    T key;
    Color color;

    Node(T key, Color color = RED) : key(key), color(color) {
        parent = nullptr;
        left = nullptr;
        right = nullptr;
    }

    Node() : Node(0) {

    }
};

template<typename T>
class RBT {
private:
    Node<T> *nil;
    Node<T> *root;
public:
    RBT() {
        nil = new Node<T>(0, BLACK);
        root = nil;
    }

    void leftRotate(Node<T> *x) {
        Node<T> *y = x->right;
        x->right = y->left;

        if (y->left != nil) {
            y->left->parent = x;
        }

        y->parent = x->parent;

        if (x->parent == nil) {
            root = y;
        } else if (x == x->parent->left) {
            x->parent->left = y;
        } else {
            x->parent->right = y;
        }

        y->left = x;
        x->parent = y;
    }

    void rightRotate(Node<T> *y) {
        Node<T> *x = y->left;
        y->left = x->right;

        if (y->left != nil) {
            y->left->parent = x;
        }

        x->parent = y->parent;

        if (y->parent == nil) {
            root = x;
        } else if (y->parent->left == y) {
            y->parent->left = x;
        } else {
            y->parent->right = x;
        }

        x->right = y;
        y->parent = x;
    }

    void insert(Node<T> *z) {
        Node<T> *y = nil;
        Node<T> *x = root;

        while (x != nil) {
            y = x;
            if (z->key < x->key)
                x = x->left;
            else
                x = x->right;
        }

        z->parent = y;
        if (y == nil) {
            root = z;
        } else if (z->key < y->key) {
            y->left = z;
        } else {
            y->right = z;
        }

        z->left = nil;
        z->right = nil;
        z->color = RED;
        insert_fixup(z);
    }

    void insert_fixup(Node<T> *z) {
        while (z->parent->color == RED) {
            if (z->parent == z->parent->parent->left) {
                Node<T> *y = z->parent->parent->right;
                if (y->color == RED) {
                    z->parent->color = BLACK;
                    y->color = BLACK;
                    z->parent->parent->color = RED;
                    z = z->parent->parent;
                } else {
                    if (z == z->parent->right) {
                        z = z->parent;
                        leftRotate(z);
                    }
                    z->parent->color = BLACK;
                    z->parent->parent->color = RED;
                    rightRotate(z->parent->parent);
                }

            } else {
                Node<T> *y = z->parent->parent->left;
                if (y->color == RED) {
                    z->parent->color = BLACK;
                    y->color = BLACK;
                    z->parent->parent->color = RED;
                    z = z->parent->parent;
                } else {
                    if (z == z->parent->left) {
                        z = z->parent;
                        rightRotate(z);
                    }
                    z->parent->color = BLACK;
                    z->parent->parent->color = RED;
                    leftRotate(z->parent->parent);
                }
            }
        }
        root->color = BLACK;
    }

    void transplant(Node<T> *u, Node<T> *v) {
        if (u->parent == nil)
            root = v;
        else if (u->parent->left == u)
            u->parent->left = v;
        else
            u->parent->right = v;
        v->parent = u->parent;
    }

    Node<T> *minimum(Node<T> *u) {
        while (u != nil && u->left != nil)
            u = u->left;
        return u;
    }

    void remove(Node<T> *z) {
        Node<T> *y = z, *x;
        Color origin_y = y->color;

        if (z->left == nil) {
            x = z->right;
            transplant(z, z->right);
        } else if (z->right == nil) {
            x = z->left;
            transplant(z, z->left);
        } else {
            y = minimum(z->right);
            origin_y = y->color;
            x = y->right;
            if (y->parent == z)
                x->parent = z;
            else {
                transplant(y, y->right);
                y->left = z->left;
                y->left->parent = y;
                y->color = z->color;
            }
            transplant(z, y);
            y->left = z->left;
            y->left->parent = y;
            y->color = z->color;
        }

        if (origin_y == BLACK) {
            remove_fixup(x);
        }
    }

    void remove_fixup(Node<T> *x) {
        while (x != root && x->color == BLACK) {
            if (x == x->parent->left) {
                Node<T> *w = x->parent->right;

                if (w->color == RED) {
                    w->color = BLACK;
                    x->parent->color = RED;
                    leftRotate(x->parent);
                    w = x->parent->right;
                }

                if (w->left->color == BLACK && w->right->color == BLACK) {
                    w->color = RED;
                    x = x->parent;
                } else {
                    if (w->right->color == BLACK) {
                        w->left->color = BLACK;
                        w->color = RED;
                        rightRotate(w);
                        w = x->parent->right;
                    }
                    w->color = x->parent->color;
                    x->parent->color = BLACK;
                    w->right->color = BLACK;
                    leftRotate(x->parent);
                    x = root;
                }
            } else {
                Node<T> *w = x->parent->left;

                if (w->color == RED) {
                    w->color = BLACK;
                    x->parent->color = RED;
                    rightRotate(x->parent);
                    w = x->parent->left;
                }

                if (w->left->color == BLACK && w->right->color == BLACK) {
                    w->color = RED;
                    x = x->parent;
                } else {
                    if (w->left->color == BLACK) {
                        w->right->color = BLACK;
                        w->color = RED;
                        leftRotate(w);
                        w = x->parent->left;
                    }
                    w->color = x->parent->color;
                    x->parent->color = BLACK;
                    w->left->color = BLACK;
                    rightRotate(x->parent);
                    x = root;
                }

            }
        }
        x->color = BLACK;
    }
};

// test for number 1-100
int main() {
    auto *nodes = new Node<int>[100];
    for (int i = 0; i < 100; ++i)
        (nodes + i)->key = i + 1;
    RBT<int> T;
    for (int i = 0; i < 100; ++i) {
        T.insert(nodes + i);
    }

    for (int i = 0; i < 95; ++i)
        T.remove(nodes + i);

    return 0;
}
```


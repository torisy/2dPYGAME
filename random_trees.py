import pygame
import random

class RandomTrees:
    def __init__(self, screen_width, screen_height, tree_size, num_trees):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tree_size = tree_size
        self.num_trees = num_trees
        self.trees = self.generate_random_trees()

    def generate_random_trees(self):
        trees = []
        for _ in range(self.num_trees):
            x = random.randint(0, self.screen_width - self.tree_size)
            y = random.randint(0, self.screen_height - self.tree_size)
            trees.append((x, y))
        return trees

    def draw(self, surface):
        for tree in self.trees:
            pygame.draw.rect(surface, (34, 139, 34), (tree[0], tree[1], self.tree_size, self.tree_size))

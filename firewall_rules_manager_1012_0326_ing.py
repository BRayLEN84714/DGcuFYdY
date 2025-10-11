# 代码生成时间: 2025-10-12 03:26:25
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QAbstractListModel, QModelIndex
from PyQt5.QtCore import Qt

"""
Firewall Rules Manager using PyQt5

This application allows users to manage firewall rules.
It provides a simple GUI interface to add, remove, and view rules.
"""

class RuleListModel(QAbstractListModel):
    """Model to manage the list of firewall rules."""
    def __init__(self, rules=None):
        super().__init__()
        self._rules = rules or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._rules)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._rules[index.row()]
        return None

    def addRule(self, rule):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._rules.append(rule)
        self.endInsertRows()

    def removeRow(self, row):
        self.beginRemoveRows(QModelIndex(), row, row)
        self._rules.pop(row)
        self.endRemoveRows()

    def getRules(self):
        return self._rules.copy()

class FirewallRulesManager(QWidget):
    "
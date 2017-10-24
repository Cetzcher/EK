from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTextEdit, QGroupBox, QLineEdit,QPushButton
from PyQt5.QtCore import Qt


class CurrentChatView(QWidget):

    def __init__(self, parent, chats):
        QWidget.__init__(self, parent)
        self.setMinimumWidth(900)
        self.setMinimumHeight(600)
        layout = QGridLayout()
        # add a panel to display the state of the current chat.

        members = QLabel("Members: you")
        members.setAlignment(Qt.AlignCenter)
        layout.addWidget(members, 0, 0)

        chatBox = QTextEdit()
        chatBox.setReadOnly(True)
        layout.addWidget(chatBox, 1, 0)
        txt = ""
        for chat in chats:
            msg, sent_by = chat["msg"], chat["sent_by"]
            txt += sent_by + ": " + msg + "\n"
        chatBox.setText(txt)


        gb = QGroupBox()
        gb_layout = QGridLayout()
        reply = QLineEdit()
        submit = QPushButton("submit")
        def on_reply():
            parent.update_text("you said: " + reply.text())
            parent.on_send_msg(reply.text())

        submit.clicked.connect(on_reply)
        gb_layout.addWidget(reply, 0, 0)
        gb_layout.addWidget(submit, 0, 1)
        gb.setLayout(gb_layout)
        layout.addWidget(gb)

        self.chatbox = chatBox

        self.setLayout(layout)

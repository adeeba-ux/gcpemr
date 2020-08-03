import PySide2.QtGui as qtGui
import PySide2.QtWidgets as qtW
import PySide2.QtCore as qtCore
import PySide2.QtPrintSupport as qtPrint

import os
import sys
import uuid

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]
IMAGE_EXTENSIONS = ['.jpg', '.png', '.bmp']
HTML_EXTENSIONS = ['.htm', '.html']
TOOLBAR_ICONSIZE = 32


def hexuuid():
    return uuid.uuid4().hex


def splitext(p):
    return os.path.splitext(p)[1].lower()


class TextEdit(qtW.QTextEdit):

    def canInsertFromMimeData(self, source):

        if source.hasImage():
            return True
        else:
            return super(TextEdit, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source):

        cursor = self.textCursor()
        document = self.document()

        if source.hasUrls():

            for u in source.urls():
                file_ext = splitext(str(u.toLocalFile()))
                if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
                    image = qtGui.QImage(u.toLocalFile())
                    document.addResource(qtGui.QTextDocument.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())

                else:
                    # If we hit a non-image or non-local URL break the loop and fall out
                    # to the super call & let Qt handle it
                    break

            else:
                # If all were valid images, finish here.
                return

        elif source.hasImage():
            image = source.imageData()
            uuid = hexuuid()
            document.addResource(qtGui.QTextDocument.ImageResource, uuid, image)
            cursor.insertImage(uuid)
            return

        super(TextEdit, self).insertFromMimeData(source)


class MainWindow(qtW.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = qtW.QVBoxLayout()
        self.editor = TextEdit()
        # Setup the QTextEdit editor configuration
        self.editor.setAutoFormatting(qtW.QTextEdit.AutoAll)
        self.editor.selectionChanged.connect(self.update_format)
        # Initialize default font size.
        font = qtGui.QFont('Arial', 12)
        self.editor.setFont(font)
        # We need to repeat the size to init the current format.
        self.editor.setFontPointSize(12)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

        layout.addWidget(self.editor)

        container = qtW.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = qtW.QStatusBar()
        self.setStatusBar(self.status)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_toolbar = qtW.QToolBar("Menu")
        file_toolbar.setIconSize(qtCore.QSize(TOOLBAR_ICONSIZE, TOOLBAR_ICONSIZE))
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&Menu")

        save_file_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'disk.png')), "Salvar", self)
        save_file_action.setStatusTip("Salvar")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        print_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'printer.png')), "Imprimir...", self)
        print_action.setStatusTip("Imprimir")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)
        file_toolbar.addAction(print_action)

        print_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'printer.png')), "Imprimir...", self)
        print_action.setStatusTip("Imprimir")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)
        file_toolbar.addAction(print_action)

        edit_toolbar = qtW.QToolBar("Editar")
        edit_toolbar.setIconSize(qtCore.QSize(TOOLBAR_ICONSIZE, TOOLBAR_ICONSIZE))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Editar")

        undo_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'arrow-curve-180-left.png')), "Desfazer", self)
        undo_action.setStatusTip("Desfazer")
        undo_action.triggered.connect(self.editor.undo)
        edit_toolbar.addAction(undo_action)
        edit_menu.addAction(undo_action)

        redo_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'arrow-curve.png')), "Refazer", self)
        redo_action.setStatusTip("Refazer")
        redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        cut_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'scissors.png')), "Cortar", self)
        cut_action.setStatusTip("Cortar texto selecionado")
        cut_action.setShortcut(qtGui.QKeySequence.Cut)
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)

        copy_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'document-copy.png')), "Copiar", self)
        copy_action.setStatusTip("Copiar texto selecionado")
        cut_action.setShortcut(qtGui.QKeySequence.Copy)
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)

        paste_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'clipboard-paste-document-text.png')), "Colar",
                                   self)
        paste_action.setStatusTip("Colar")
        cut_action.setShortcut(qtGui.QKeySequence.Paste)
        paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)

        select_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'selection-input.png')), "Selecionar tudo", self)
        select_action.setStatusTip("Selecionar todo o texto")
        cut_action.setShortcut(qtGui.QKeySequence.SelectAll)
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)

        edit_menu.addSeparator()

        wrap_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'arrow-continue.png')), "Quebra de linha",
                                  self)
        wrap_action.setStatusTip("Alternar quebra automática de texto para janela")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)
        edit_menu.addAction(wrap_action)

        format_toolbar = qtW.QToolBar("Formatar")
        format_toolbar.setIconSize(qtCore.QSize(16, 16))
        self.addToolBar(format_toolbar)
        format_menu = self.menuBar().addMenu("&Formatar")

        # We need references to these actions/settings to update as selection changes, so attach to self.
        self.fonts = qtW.QFontComboBox()
        self.fonts.currentFontChanged.connect(self.editor.setCurrentFont)
        format_toolbar.addWidget(self.fonts)

        self.fontsize = qtW.QComboBox()
        self.fontsize.addItems([str(s) for s in FONT_SIZES])

        # Connect to the signal producing the text of the current selection. Convert the string to float
        # and set as the pointsize. We could also use the index + retrieve from FONT_SIZES.
        self.fontsize.currentIndexChanged[str].connect(lambda s: self.editor.setFontPointSize(float(s)))
        format_toolbar.addWidget(self.fontsize)

        self.bold_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'edit-bold.png')), "Negrito", self)
        self.bold_action.setStatusTip("Negrito")
        self.bold_action.setShortcut(qtGui.QKeySequence.Bold)
        self.bold_action.setCheckable(True)
        self.bold_action.toggled.connect(
            lambda x: self.editor.setFontWeight(qtGui.QFont.Bold if x else qtGui.QFont.Normal))
        format_toolbar.addAction(self.bold_action)
        format_menu.addAction(self.bold_action)

        self.italic_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'edit-italic.png')), "Itálico", self)
        self.italic_action.setStatusTip("Itálico")
        self.italic_action.setShortcut(qtGui.QKeySequence.Italic)
        self.italic_action.setCheckable(True)
        self.italic_action.toggled.connect(self.editor.setFontItalic)
        format_toolbar.addAction(self.italic_action)
        format_menu.addAction(self.italic_action)

        self.underline_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'edit-underline.png')), "Sublinhar",
                                            self)
        self.underline_action.setStatusTip("Sublinhar")
        self.underline_action.setShortcut(qtGui.QKeySequence.Underline)
        self.underline_action.setCheckable(True)
        self.underline_action.toggled.connect(self.editor.setFontUnderline)
        format_toolbar.addAction(self.underline_action)
        format_menu.addAction(self.underline_action)

        format_menu.addSeparator()

        self.alignl_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'edit-alignment.png')), "Alinhar à esquerda", self)
        self.alignl_action.setStatusTip("Alinhar texto à esquerda")
        self.alignl_action.setCheckable(True)
        self.alignl_action.triggered.connect(lambda: self.editor.setAlignment(qtCore.Qt.AlignLeft))
        format_toolbar.addAction(self.alignl_action)
        format_menu.addAction(self.alignl_action)

        self.alignc_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'edit-alignment-center.png')),
                                         "Alinhar ao centro", self)
        self.alignc_action.setStatusTip("Alinhar texto ao centro")
        self.alignc_action.setCheckable(True)
        self.alignc_action.triggered.connect(lambda: self.editor.setAlignment(qtCore.Qt.AlignCenter))
        format_toolbar.addAction(self.alignc_action)
        format_menu.addAction(self.alignc_action)

        self.alignr_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'edit-alignment-right.png')), "Alinhar à direita", self)
        self.alignr_action.setStatusTip("Alinhar texto à direita")
        self.alignr_action.setCheckable(True)
        self.alignr_action.triggered.connect(lambda: self.editor.setAlignment(qtCore.Qt.AlignRight))
        format_toolbar.addAction(self.alignr_action)
        format_menu.addAction(self.alignr_action)

        self.alignj_action = qtW.QAction(qtGui.QIcon(os.path.join('images', 'edit-alignment-justify.png')), "Justificar", self)
        self.alignj_action.setStatusTip("Justificar texto")
        self.alignj_action.setCheckable(True)
        self.alignj_action.triggered.connect(lambda: self.editor.setAlignment(qtCore.Qt.AlignJustify))
        format_toolbar.addAction(self.alignj_action)
        format_menu.addAction(self.alignj_action)

        format_group = qtW.QActionGroup(self)
        format_group.setExclusive(True)
        format_group.addAction(self.alignl_action)
        format_group.addAction(self.alignc_action)
        format_group.addAction(self.alignr_action)
        format_group.addAction(self.alignj_action)

        format_menu.addSeparator()

        # A list of all format-related widgets/actions, so we can disable/enable signals when updating.
        self._format_actions = [
            self.fonts,
            self.fontsize,
            self.bold_action,
            self.italic_action,
            self.underline_action,
            # We don't need to disable signals for alignment, as they are paragraph-wide.
        ]

        # Initialize.
        self.update_format()
        self.update_title()
        self.show()

    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    def update_format(self):
        """
        Update the font format toolbar/actions when a new text selection is made. This is neccessary to keep
        toolbars/etc. in sync with the current edit state.
        :return:
        """
        # Disable signals for all format widgets, so changing values here does not trigger further formatting.
        self.block_signals(self._format_actions, True)

        self.fonts.setCurrentFont(self.editor.currentFont())
        # Nasty, but we get the font-size as a float but want it was an int
        self.fontsize.setCurrentText(str(int(self.editor.fontPointSize())))

        self.italic_action.setChecked(self.editor.fontItalic())
        self.underline_action.setChecked(self.editor.fontUnderline())
        self.bold_action.setChecked(self.editor.fontWeight() == qtGui.QFont.Bold)

        self.alignl_action.setChecked(self.editor.alignment() == qtCore.Qt.AlignLeft)
        self.alignc_action.setChecked(self.editor.alignment() == qtCore.Qt.AlignCenter)
        self.alignr_action.setChecked(self.editor.alignment() == qtCore.Qt.AlignRight)
        self.alignj_action.setChecked(self.editor.alignment() == qtCore.Qt.AlignJustify)

        self.block_signals(self._format_actions, False)

    def dialog_critical(self, s):
        dlg = qtCore.QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(qtCore.QMessageBox.Critical)
        dlg.show()

    def file_save(self):
        # text = self.editor.toHtml()
        # record_ctrl = _ctrls.RecordCtrl(_db.session)

        # record_ctrl.add()
        pass

    def file_print(self):
        dlg = qtPrint.QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())

    def update_title(self):
        # get user and patient names to update title
        pass

    def edit_toggle_wrap(self):
        if self.editor.lineWrapMode() == qtW.QTextEdit.LineWrapMode.WidgetWidth:
            self.editor.setLineWrapMode(self.editor.lineWrapMode().NoWrap)
        else:
            self.editor.setLineWrapMode(self.editor.lineWrapMode().WidgetWidth)


if __name__ == '__main__':
    app = qtW.QApplication(sys.argv)
    app.setApplicationName("Novo Prontuario")

    window = MainWindow()
    app.exec_()

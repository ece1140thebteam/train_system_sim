import QtQuick 2.7
import QtQuick.Layouts 1.2

import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12


ApplicationWindow {
    id: trackModel
    width: 1200; height: 600
    visible: true
    property var trackFile: track_file_binding.text
    title: "Track Model Test"

    ComboBox {
        currentIndex: 2
        model: ListModel {
            id: cbItems
            ListElement { text: "Banana"; color: "Yellow" }
            ListElement { text: "Apple"; color: "Green" }
            ListElement { text: "Coconut"; color: "Brown" }
        }
        width: 200
        onCurrentIndexChanged: console.debug(cbItems.get(currentIndex).text + ", " + cbItems.get(currentIndex).color)
    }
}
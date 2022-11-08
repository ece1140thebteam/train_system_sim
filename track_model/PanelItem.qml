import QtQuick 2.7
import QtQuick.Layouts 1.2
import QtQuick.Window 2.0

Window {
    visible: true
    width: 400
    height: 400

    ColumnLayout {
        anchors.fill: parent
        spacing: 1
        property var currentItem: null
        PanelItem {
            title: "Panel 1"
            Rectangle {
                color: "orange"
                anchors.fill: parent
            }
        }
        PanelItem {
            title: "Panel 2"
            Rectangle {
                color: "lightgreen"
                anchors.fill: parent
            }
        }
        PanelItem {
            title: "Panel 3"
            Rectangle {
                color: "lightblue"
                anchors.fill: parent
            }
        }
        PanelItem {
            title: "Panel 4"
            Rectangle {
                color: "yellow"
                anchors.fill: parent
            }
        }
        Item {
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
    }
}
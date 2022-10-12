import QtQuick 2.7
import QtQuick.Layouts 1.2

import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12


ApplicationWindow {
    width: 1200; height: 600
    visible: true
    property var trackFile: "default.csv"

    RowLayout {
        id: main_windows
        anchors.fill: parent
        spacing: 0

        ColumnLayout {
            spacing: 0
            Layout.preferredWidth: main_windows.width*.3

            ColumnLayout {
                //Layout.preferredWidth: 300
                Layout.fillWidth: true
                Layout.preferredHeight: main_windows.height*.6
                // L: Layout.AlignTop

                // file selector
                RowLayout{
                    id: fileSelect
                    Layout.fillWidth: true


                    Text {
                        text: trackFile
                        horizontalAlignment: Layout.AlignLeft

                    }
                    
                    // horizontalAlignment: Layout.AlignRight

                    Button{
                        text: "Select New Track"
                        // horizontalAlignment: Layout.AlignRight
                    
                        anchors{      
                            // top: popupContent.bottom
                            // bottom: popup.bottom
                            right: fileSelect.right
                            rightMargin: 0
                            // rightMargin: 24
                            // leftMargin: 16
                            // topMargin: 24
                        }
                    }

                    
                }

                ScrollView{
                    Layout.preferredHeight: main_windows.height*.9
                    ScrollBar.vertical.policy: ScrollBar.AlwaysOn
                    Layout.fillWidth: true

                    // ColumnLayout{
                    //     Repeater {
                    //         model: line_list_manager.model

                    //         ListView {
                    //             id: trackBlock

                    //             Text {
                    //                 // required property string block
                    //                 // required property string section
                    //                 // required property string line
                    //                 width: parent.width
                    //                 Layout.preferredHeight: main_windows.height*.05

                    //                 text: model.block + ", " + model.section +", "+model.line
                    //             }
                    //         }
                    //     }
                    // }


                    // ListModel {
                    //     id: trackLineModel
                    //     ListElement { block: "1"; section: "A"; line: "Blue" }
                    //     ListElement { block: "2"; section: "A"; line: "Blue" }
                    // }

                    Component {
                        id: trackLineDelegate
                        Text {
                            required property string block
                            required property string section
                            required property string line
                            width: parent.width

                            text: block + ", " + section +", "+line
                        }
                    }
                    ListView {
                        anchors.fill: parent
                        model: line_list_manager.model
                        delegate: trackLineDelegate
                        focus: true
                        highlight: Rectangle {
                            color: "lightblue"
                            width: parent.width
                        }
                        section {
                            property: "line"
                            criteria: ViewSection.FullString
                            delegate: Rectangle {
                                color: "#b0dfb0"
                                width: parent.width
                                height: childrenRect.height + 4
                                Text { anchors.horizontalCenter: parent.horizontalCenter
                                    font.pixelSize: 16
                                    font.bold: true
                                    text: section
                                }
                            }

                        }
                    }
                }
            }

            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: main_windows.height*.4

                color: "blue"
            }
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.preferredWidth: main_windows.width*.7
            color: "red"
        }
    }
}
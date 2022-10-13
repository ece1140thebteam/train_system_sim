import QtQuick 2.7
import QtQuick.Layouts 1.2

import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12


ApplicationWindow {
    id: trackModel
    width: 500; height: 300
    visible: true

    title: "Track Model Test"
    

    ColumnLayout{
        Layout.fillWidth: true
        Layout.fillHeight: true
        RowLayout{
            spacing: 10
            // select the update type
            Rectangle{
                // topPadding: 10
                // leftPadding: 10
                Layout.leftMargin: 20
                Layout.topMargin: 20
                Layout.preferredHeight: 100
                Layout.preferredWidth: 200
                ColumnLayout{
                    spacing: 10
                    Text{
                        text: "Send update of:"
                        font.weight: Font.Black
                        font.pointSize: 16
                    }
                    ComboBox {
                        currentIndex: -1
                        
                        model: ListModel {
                            id: commandTypes
                            ListElement { text: "Authority"}
                            ListElement { text: "Commanded Speed"}
                            ListElement { text: "Switch Position"}
                            ListElement { text: "Railway Crossing"}
                            ListElement { text: "Signal"}
                            ListElement { text: "Track Maintenance"}
                            ListElement { text: "Track Heater"}
                            ListElement { text: "Track Failure"}
                            ListElement { text: "Lights"}
                            ListElement { text: "Track Circuit"}
                        }
                        width: 500
                        onCurrentIndexChanged: 
                        {
                            function_bindings.update_command_type(commandTypes.get(currentIndex).text)
                        }
                    }
                }
            }

            // Select the block
            Rectangle{
                // topPadding: 10
                // leftPadding: 10
                Layout.preferredWidth: 200
                Layout.preferredHeight: 100

                Layout.leftMargin: 20
                Layout.topMargin: 20
                ColumnLayout{
                    Text{
                        text: input_type.text
                        font.weight: Font.Black
                        font.pointSize: 16
                    }

                    TextField {
                        objectName: "updateTarget"
                        id: updateTarget
                        placeholderText: qsTr(input_type.text)
                    }
                    
                }
            }
        }

        RowLayout{
            spacing: 10
            // select the update type
                        // Select the block
            Rectangle{
                // topPadding: 10
                // leftPadding: 10
                Layout.preferredWidth: 200
                Layout.preferredHeight: 100

                Layout.leftMargin: 20
                Layout.topMargin: 20
                ColumnLayout{
                    Text{
                        text: input_field.text
                        font.weight: Font.Black
                        font.pointSize: 16
                    }

                    TextField {
                        objectName: "updateValue"
                        id: updateValue
                        placeholderText: qsTr(input_field.text)
                        font.capitalization: Font.AllLowercase 
                    }
                    
                }
            
            }
            // Select the block
            Rectangle{
                // topPadding: 10
                // leftPadding: 10
                Layout.preferredWidth: 200
                Layout.preferredHeight: 100

                Layout.leftMargin: 20
                Layout.topMargin: 20
                Layout.alignment: Qt.AlignRight
                Layout.fillWidth: true

                Button{
                    id: submitUpdate
                    text: "Send Update"
                    Layout.alignment: Qt.AlignRight
                    Layout.fillWidth: true   
                    onClicked: {
                        function_bindings.send_update(updateTarget.text, updateValue.text)
                    }
                }
            }
        }
    }


}
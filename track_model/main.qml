import QtQuick 2.7
import QtQuick.Layouts 1.2

import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12


ApplicationWindow {
    id: trackModel
    width: 1200; height: 600
    visible: true
    property var trackFile: track_file_binding.text
    title: "Track Model"

    RowLayout {
        id: main_windows
        anchors.fill: parent
        spacing: 4

        ColumnLayout {
            id: leftSideBar
            spacing: 0
            Layout.preferredWidth: main_windows.width*.2

            // block selector
            ColumnLayout {
                //Layout.preferredWidth: 300
                Layout.fillWidth: true
                Layout.preferredHeight: main_windows.height*.5

                // file selector bar
                Rectangle{
                    Layout.preferredWidth: leftSideBar.width
                    height: childrenRect.height
                    color: "#80CBC4"
                    Layout.fillWidth: true

                    RowLayout{
                        id: fileSelect
                        Layout.fillWidth: true

                        Text {
                            text: trackFile
                            horizontalAlignment: Layout.AlignLeft
                            verticalAlignment: Text.AlignVCenter
                            leftPadding: 10
                        }


                        // fill the center 
                        Item{
                            Layout.fillWidth: true
                            height: newTrackButton.implicitHeight
                        }

                        Button{
                            id: newTrackButton
                            text: "Select New Track"
                            
                            onClicked: {
                                function_bindings.open_new_file()
                            }
                        }                        
                    }
                }

                // list of blocks 
                ScrollView{
                    Layout.preferredHeight: main_windows.height
                    ScrollBar.vertical.policy: ScrollBar.AlwaysOn
                    ScrollBar.vertical.interactive: true
                    clip: true

                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    
                    Component {
                        id: trackLineDelegate

                        RowLayout{
                            required property string block
                            required property string section
                            required property string line
                        
                            Layout.preferredWidth: leftSideBar.width
                            anchors.left: parent.left

                            Rectangle
                            {
                                Layout.preferredWidth: leftSideBar.width/3
                                height: childrenRect.height
                                Text {
                                    text: line
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Rectangle
                            {
                                Layout.preferredWidth: leftSideBar.width/3
                                height: childrenRect.height
                                Text {
                                    text: section
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Rectangle
                            {
                                Layout.preferredWidth: leftSideBar.width/3
                                height: childrenRect.height
                                Text {
                                    text: block
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            MouseArea{
                                signal update_properties_required
                                anchors.fill: parent
                                hoverEnabled: true

                                onClicked: {
                                    function_bindings.select_block(line, block)
                                }
                            }
                        }
                    }
                    ListView {
                        anchors.fill: parent
                        model: line_list_manager.model
                        delegate: trackLineDelegate

                        section {
                            property: "line"
                            criteria: ViewSection.FullString
                            delegate: Rectangle {
                                color: "#009688"
                                width: parent.width
                                height: childrenRect.height + 4
                                Text { anchors.horizontalCenter: parent.horizontalCenter
                                    font.pixelSize: 16
                                    font.bold: true
                                    text: section + ' line'
                                }
                            }

                        }
                    }
                }
            }

            // selected block information
            ColumnLayout {
                Layout.fillWidth: true
                Layout.preferredHeight: main_windows.height*.5
                

                ScrollView{
                    Layout.preferredHeight: main_windows.height
                    ScrollBar.vertical.policy: ScrollBar.AlwaysOn
                    ScrollBar.vertical.interactive: true
                    clip: true
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    background: Rectangle {
                            color: "#607D8B"
                    }

                    Component {
                        id: blockInfoDelegate

                        // RowLayout{
                            
                        ColumnLayout{
                            spacing: 0
                            required property string title
                            required property string detail
                        
                            Layout.preferredWidth: leftSideBar.width
                            anchors.left: parent.left
                            Rectangle
                            {
                                Layout.preferredWidth: leftSideBar.width
                                height: childrenRect.height
                                color: "#607D8B"

                                Text {
                                    topPadding: 4
                                    leftPadding: 4
                                    text: title
                                    color: "white"
                                    font.pointSize: 14
                                    font.bold: true
                                    horizontalAlignment: Layout.AlignLeft
                                }
                            }

                            Rectangle
                            {
                                Layout.preferredWidth: leftSideBar.width
                                height: childrenRect.height
                                color: "#607D8B"

                                Text {
                                    text: detail
                                    color: "white"
                                    font.pointSize: 12
                                    leftPadding: 6
                                    horizontalAlignment: Layout.AlignLeft

                                    // anchors.horizontalCenter: parent.left
                                }
                            }
                        }

                    }

                    ListView {
                        anchors.fill: parent
                        model: displayed_block_manager.model
                        delegate: blockInfoDelegate
                    }
                }
            }

            // create a failure
            ColumnLayout{
                Rectangle
                {
                    height: childrenRect.height
                    Layout.fillWidth: true
                    color: "#607D8B"
                    
                    RowLayout
                    {
                        Button{
                            text: "Break Rail"
                            
                            background: Rectangle {
                                color: parent.down ? "#bbbbbb" :
                                    (parent.hovered ? "#d6d6d6" : "#f6f6f6")
                            }
                            onClicked: {
                                function_bindings.create_failure("Broken Rail")
                            }
                        }
                        Item{
                            Layout.fillWidth: true
                        }
                        Button{
                            text: "Power Failure"
                            background: Rectangle {
                                color: parent.down ? "#bbbbbb" :
                                    (parent.hovered ? "#d6d6d6" : "#f6f6f6")
                            }
                            onClicked: {
                                function_bindings.create_failure("Power Failure")
                            }
                        }  
                    
                    }
                }
                Rectangle{
                    height: childrenRect.height
                    Layout.fillWidth: true
                    color: "#607D8B"
                    RowLayout
                    {
                        Button{
                            text: "Track Circuit Failure"
                            background: Rectangle {
                                color: parent.down ? "#bbbbbb" :
                                    (parent.hovered ? "#d6d6d6" : "#f6f6f6")
                            }
                            onClicked: {
                                function_bindings.create_failure("Track Circuit Failure")
                            }
                        }
                        Button{
                            text: "No Failure"
                            background: Rectangle {
                                color: parent.down ? "#bbbbbb" :
                                    (parent.hovered ? "#d6d6d6" : "#f6f6f6")
                            }
                            onClicked: {
                                print('helo')
                                function_bindings.create_failure("No Failure")
                            }
                        } 
                    }
                }

            }
        }
    
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.preferredWidth: main_windows.width*.8
            // color: "red"
        }
    }
}
import QtQuick 2.0
import QtQuick.Window 2.0
//import QtQuick.Controls 2.0

Image{
    source: "mainLoading.png"
    Text {
    id: element
    text: "downloding resources..."
    anchors.top: parent.top
    color:"white"
    font.pixelSize: 15
    font.bold:True
    horizontalAlignment: Text.AlignHCenter
    verticalAlignment: Text.AlignVCenter
    anchors.topMargin: 200
    anchors.horizontalCenter: parent.horizontalCenter
}
}

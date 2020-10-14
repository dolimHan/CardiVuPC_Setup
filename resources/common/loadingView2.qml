import QtQuick 2.0
import QtQuick.Window 2.0

Rectangle {
    color:"#00bfa5"

    visible:true
    anchors.centerIn: parent
    width: 700   // 부모(Window)의 폭을 사용
    height: 231 // 부모(Window)의 높이를 사용

    Row {
        spacing:20
        anchors.centerIn: parent
        Text {
            id: loadingSpinner
            text: "◠"
            font.pixelSize: 100
            color: "#ffffff"
            anchors.verticalCenter: parent.verticalCenter
            font.bold: true
            NumberAnimation on rotation {
                from: 0; to: 360; running: loadingSpinner.visible == true;
                loops: Animation.Infinite; duration: 700;
            }
        }
        // Text explaining whats happening
        Text {
            text: "Loading..."
            font.family: "Noto Sans CJK KR Bold"
            font.pixelSize: 23
            color: "#ffffff"
            anchors.verticalCenter: parent.verticalCenter
            font.letterSpacing:3
        }
    }
}
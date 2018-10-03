package demo;

import java.util.ArrayList;

public class ArrayCollection {
	
	

	public static void main(String[] args) {
		 ArrayList<Integer> obj = new ArrayList<Integer>();
		 for(int i=5;i<=100;i=i+5)
		 {
			 obj.add(i);
		 }
System.out.println(obj);
		
	}

}
/*
public function createComboBox_clickHandler(event:Event):void {
var myComboBox:ComboBox = new ComboBox();
var comboBoxDataProvider:ArrayCollection =new ArrayCollection([
    { name: "box1", value: "value1"},
    { name: "box2", value: "value2"},
    { name: "box3", value: "value3"},
    { name: "box4", value: "value4"}
]);

myComboBox.x = 100;
myComboBox.y = 100;
myComboBox.dataProvider = comboBoxDataProvider;
myComboBox.labelField = "name";
myComboBox.addEventListener(ListEvent.CHANGE, myComboBox_ClickHandler);
container.addElement(myComboBox);
}

public function myComboBox_ClickHandler(event:ListEvent):void{
trace(event.currentTarget.selectedItem.value);
}
*/

/*
<s:ComboBox id="myCB"> 
<s:ArrayList id="stateArray">
    <fx:Object label="AL" data="Montgomery"/>
    <fx:Object label="AK" data="Juneau"/>
    <fx:Object label="AR" data="Little Rock"/>
</s:ArrayList>
</s:ComboBox>
*/
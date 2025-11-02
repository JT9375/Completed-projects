using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class AnswerScript0 : MonoBehaviour
{

    public questionScript Qscript;



    private void OnCollisionEnter2D(Collision2D collision)
    {  

        if(collision.gameObject.layer == 6 && Qscript.Location == 0)
        {
            Qscript.Score();
            Debug.Log("Score Increaced");
            Qscript.QuestionSelect();
        }

        else if(collision.gameObject.layer == 6 && Qscript.Location != 0)
        {
            Qscript.Fail();
        }


    }


}

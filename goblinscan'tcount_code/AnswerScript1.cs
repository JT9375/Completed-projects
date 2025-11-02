using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class AnswerScript1 : MonoBehaviour
{

    public questionScript Qscript;



    private void OnCollisionEnter2D(Collision2D collision)
    {

        if (collision.gameObject.layer == 6 && Qscript.Location == 1)
        {
            Qscript.Score();
            Debug.Log("Score Increaced");
            Qscript.QuestionSelect();
        }

        else if(collision.gameObject.layer == 6 && Qscript.Location != 1)
        {
            Qscript.Fail();
        }

    }


}
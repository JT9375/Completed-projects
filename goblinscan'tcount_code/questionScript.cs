using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class questionScript : MonoBehaviour
{
    private float randomnum1;
    private float randomnum2;
    public float Answer = 0;
    public float FA = 0;
    public Text questiontext;
    public Text AnswerText0;
    public Text AnswerText1;
    public Text ScoreText;
    public int Location;
    public int score = 0;
    public int Health = 3;
    public SavedData SD;
    public int Questionselect;
    public GameObject Goblin;
    public GameObject QuestionUI;
    public GameObject PauseMenu;

    // Start is called before the first frame update
    void Start()
    {
        score = 0;
        ScoreText.text = score.ToString();
        QuestionSelect();
    }

    //Activates the pause menu
    private void Update()
    {
        if(Input.GetKeyUp(KeyCode.Escape))
        {
            Goblin.SetActive(false);
            QuestionUI.SetActive(false);
            PauseMenu.SetActive(true);
        }
    }

    //Selects the question type using a randomly generated number
    public void QuestionSelect()
    {
        Questionselect = Random.Range(0, 4);

        if(Questionselect == 0)
        {
            GenerateQ();
        }

        else if(Questionselect == 1)
        {
            GenerateQSubtract();
        }

        else if(Questionselect == 2)
        {
            GenerateQMultiply();
        }

        else if(Questionselect == 3)
        {
            GenerateQDivide();
        }
    }

    //generates an addition question
    [ContextMenu ("generate addition Question")]
    public void GenerateQ()
    {
        //generates 2 random numbers and calculates the answer
        randomnum1 = Random.Range(1, 101);
        randomnum2 = Random.Range(1, 101);
        //Decides where the correct answer will be located
        Location = Random.Range(0, 2);
        //calculates the answer
        Answer = randomnum1 + randomnum2;
        //Activates the fake answer function
        FakeAnswer();
        //activates answerlocation function
        AnswerLocation();
        //turns a string in c# into text for the unity editor to display within the UI
        questiontext.text = string.Format("What is {0} + {1}?", randomnum1, randomnum2);

    }

    //Generates a subtraction question
    [ContextMenu ("generate subtraction Question")]
    public void GenerateQSubtract()
    {
        //generates 2 random numbers and calculates the answer
        randomnum1 = Random.Range(1, 101);
        randomnum2 = Random.Range(1, 101);
        //Decides where the correct answer will be located
        Location = Random.Range(0, 2);
        //calculates the answer
        Answer = randomnum1 - randomnum2;
        //Activates the fake answer function
        FakeAnswer();
        //activates answerlocation function
        AnswerLocation();
        //turns a string in c# into text for the unity editor to display within the UI
        questiontext.text = string.Format("What is {0} - {1}?", randomnum1, randomnum2);

    }

    //generates a multiplication question
    [ContextMenu("generate multiplication Question")]
    public void GenerateQMultiply()
    {
        //generates 2 random numbers and calculates the answer
        randomnum1 = Random.Range(1, 101);
        randomnum2 = Random.Range(1, 101);
        //Decides where the correct answer will be located
        Location = Random.Range(0, 2);
        //calculates the answer
        Answer = randomnum1 * randomnum2;
        //Activates the fake answer function
        FakeAnswer();
        //activates answerlocation function
        AnswerLocation();
        //turns a string in c# into text for the unity editor to display within the UI
        questiontext.text = string.Format("What is {0} * {1}?", randomnum1, randomnum2);

    }

    //generates a division question
    [ContextMenu("generate division Question")]
    public void GenerateQDivide()
    {
        //generates 2 random numbers and calculates the answer
        randomnum1 = Random.Range(50, 101);
        randomnum2 = Random.Range(1, 51);
        //Decides where the correct answer will be located
        Location = Random.Range(0, 2);
        //calculates the answer
        Answer = randomnum1 / randomnum2;
        //Activates the fake answer function
        FakeAnswer();
        //activates answerlocation function
        AnswerLocation();
        //turns a string in c# into text for the unity editor to display within the UI
        questiontext.text = string.Format("What is {0} / {1} rounded?", randomnum1, randomnum2);

    }

    //Adds to the score and checks if score is over 10 it changes to the next level of questions
    public void Score()
    {
        score = score + 1;
        ScoreText.text = score.ToString();
        if(score >= 10)
        {
            SceneManager.LoadScene(4);
        }
        SD.UpdateData1();
        QuestionSelect();
    }

    //checks player's health and determines if it should trigger game over or remove a life
    public void Fail()
    {
        if(Health != 0)
        {
            Health = Health - 1;
            SD.UpdateData1();
            SceneManager.LoadScene(1);
        }

        else
        {
            SceneManager.LoadScene(2);
        }
    }

    //Selects the location of the correct and incorrect answer
    public void AnswerLocation()
    {
        if(Location == 0)
        {
            Debug.Log("correct answer on left");
            AnswerText0.text = Answer.ToString();
            AnswerText1.text = FA.ToString();
        }

        if (Location == 1)
        {
            Debug.Log("Correct Answer on right");
            AnswerText1.text = Answer.ToString();
            AnswerText0.text = FA.ToString();
        }
    }

    //creates a fake answer and checks to see if it matches the correct answer. If it does, Fake answer is regenerated until they dont match
    public void FakeAnswer()
    {
        FA = Answer + Random.Range(-5, 5);

        while(FA == Answer)
        {
            FA = Answer + Random.Range(-5, 5);
        }
    }
    
}

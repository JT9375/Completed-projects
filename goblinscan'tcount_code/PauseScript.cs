using System.Collections;
using System.Collections.Generic;
using System.Net;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class PauseScript : MonoBehaviour
{
    public GameObject Goblin;
    public GameObject QuestionUI;
    public GameObject PauseUI;

    //Activates the pause menu
    private void Update()
    {
        if(Input.GetKeyDown(KeyCode.Escape))
        {
            Goblin.SetActive(false);
            QuestionUI.SetActive(false);
            PauseUI.SetActive(true);
        }
    }

    public void ContinueGame()
    {
        Goblin.SetActive(true);
        QuestionUI.SetActive(true);
        PauseUI.SetActive(false);
    }

    public void EndGame()
    {
        SceneManager.LoadScene(3);
    }
}

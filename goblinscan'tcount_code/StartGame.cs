using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using Unity.VisualScripting;

public class StartGame : MonoBehaviour
{
    public void startgame()
    {
        SceneManager.LoadScene(0);
    }

    public void HTP()
    {
        SceneManager.LoadScene(5);
    }

    public void EndGame() 
    {
        Application.Quit();
    }
}

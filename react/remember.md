# Points to remember in react

* Never change the state of the application directly. Always use ``` this.setState()``` function to change the state.
* If we want to make a copy of a list then use this,
    ``` const list1 = [1, 2, 3, 4, 5];
        const copy = [...list1];
    ```
* If we want to make a copy and add something to the copy then,
    ``` const list1 = [1, 2, 3, 4, 5];
        const list2 = [...list1, 6];
    ```
* To delete something from the list
    ``` const list1 = [1, 2, 3, 4, 5];
        list.splice(3, 1);

        // list1 is now [1, 2, 3, 5]
    ```
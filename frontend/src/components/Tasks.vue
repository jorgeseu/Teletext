<template>
    <div class="tasks_container">
    <div class="add_task">
        <form v-on:submit.prevent="submitForm">
            <div class="form-group">
                <label for="program_ID">Program_ID</label>
                <input type="text" class="form-control" id="program_ID" v-model="program_ID">
            </div>
            <div class="form-group">
                <label for="program_date">Program Date</label>
                <textarea class="form-control" id="program_date" v-model="program_date"></textarea>
            </div>
            <div class="form-group">
                <button type="submit">Add Program</button>
            </div>
        </form>
    </div>
        <div class="tasks_content">
            <h1>ProgramItems</h1>
            <ul class="tasks_list">
                <li v-for="ProgramItem in ProgramItems" :key="ProgramItem.id">
                    <h2>{{ ProgramItem.program_ID }}</h2>
                    <p>{{ ProgramItem.program_date }}</p>
                    <button @click="toggleProgramItem(ProgramItem)">
                        {{ ProgramItem.program_data ? 'Undo' : 'Complete' }}
                    </button>
                    <button @click="deleteProgramItem(ProgramItem)">Delete</button>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                // tasks
                ProgramItems: [],
                program_ID: '',
                program_date: ''
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch tasks
                    const response = await this.$http.get('http://45.9.188.43/api/ProgramItems/');
                    // set the data returned as tasks
                    this.ProgramItems = response.data;
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
            async submitForm(){
                try {
                    // Send a POST request to the API
                    const response = await this.$http.post('http://45.9.188.43/api/ProgramItems/', {
                        title: this.program_ID,
                        description: this.program_date,
                        program_data: false
                    });
                    // Append the returned data to the tasks array
                    this.ProgramItems.push(response.data);
                    // Reset the title and description field values.
                    this.program_ID = '';
                    this.program_date = '';
                } catch (error) {
                    // Log the error
                    console.log(error);
                }
            },
            async toggleProgramItem(ProgramItem){
                try{

                    // Send a request to API to update the task
                    const response = await this.$http.put(`http://45.9.188.43/api/ProgramItems/${ProgramItem.id}/`, {
                        completed: !ProgramItem.program_data,
                        program_ID: ProgramItem.program_ID,
                        program_date: ProgramItem.program_date
                    });

                    // Get the index of the task being updated
                    let ProgramItemIndex = this.ProgramItems.findIndex(t => t.id === ProgramItem.id);

                    // Reset the tasks array with the new data of the updated task

                    this.ProgramItems = this.ProgramItems.map((ProgramItem) => {
                        if(this.ProgramItems.findIndex(t => t.id === ProgramItem.id) === ProgramItemIndex){
                            return response.data;
                        }
                        return ProgramItem;
                    });

                }catch(error){

                    // Log any error
                    console.log(error);
                }
            },
            async deleteProgramItem(ProgramItem){

                // Confirm if one wants to delete the task
                let confirmation = confirm("Do you want to delete this ProgramItem?");

                if(confirmation){
                    try{

                    // Send a request to delete the task
                    await this.$http.delete(`http://45.9.188.43/api/ProgramItems/${ProgramItem.id}`);

                    // Refresh the tasks
                    this.getData();
                    }catch(error){

                    // Log any error

                    console.log(error)
                    }
                }
            },
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>